#!/usr/bin/env python3
"""
Sync accepted LeetCode submissions into this repository.

This intentionally avoids third-party GitHub Actions. It talks directly to
LeetCode's GraphQL API using the user's LEETCODE_SESSION and CSRF token.

The script is idempotent: existing solution files are never duplicated.
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / "leetcode-solutions"

SESSION = os.environ.get("LEETCODE_SESSION", "").strip()
CSRF = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()

GRAPHQL_URL = "https://leetcode.com/graphql/"
PAGE_SIZE = 20
MAX_RETRIES = 5
LANG_TO_EXTENSION = {
    "bash": "sh", "c": "c", "cpp": "cpp", "csharp": "cs", "dart": "dart",
    "elixir": "ex", "erlang": "erl", "golang": "go", "java": "java",
    "javascript": "js", "kotlin": "kt", "mssql": "sql", "mysql": "sql",
    "oraclesql": "sql", "php": "php", "python": "py", "python3": "py",
    "pythondata": "py", "postgresql": "sql", "racket": "rkt", "ruby": "rb",
    "rust": "rs", "scala": "scala", "swift": "swift", "typescript": "ts",
}


def die(message):
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def headers():
    if not SESSION or not CSRF:
        die(
            "Missing LEETCODE_SESSION or LEETCODE_CSRF_TOKEN. "
            "Refresh the LeetCode cookies and update the GitHub Actions secrets."
        )
    return {
        "Content-Type": "application/json",
        "Origin": "https://leetcode.com",
        "Referer": "https://leetcode.com/",
        "User-Agent": "Mozilla/5.0 LeetCode-GitHub-Sync",
        "Cookie": f"csrftoken={CSRF}; LEETCODE_SESSION={SESSION};",
        "x-csrftoken": CSRF,
    }


def graphql(query, variables):
    payload = json.dumps({"query": query, "variables": variables}).encode()
    for attempt in range(MAX_RETRIES + 1):
        try:
            req = Request(GRAPHQL_URL, data=payload, headers=headers(), method="POST")
            with urlopen(req, timeout=30) as response:
                body = json.loads(response.read().decode("utf-8"))

            if body.get("errors"):
                messages = "; ".join(
                    str(e.get("message", "GraphQL error")) for e in body["errors"]
                )
                if "login" in messages.lower() or "unauthorized" in messages.lower():
                    die("LeetCode rejected the session. Refresh LEETCODE_SESSION.")
                raise RuntimeError(messages)

            data = body.get("data")
            if data is None:
                die(
                    "LeetCode returned no data. Your session may have expired. "
                    "Refresh LEETCODE_SESSION and LEETCODE_CSRF_TOKEN."
                )
            return data

        except HTTPError as exc:
            if exc.code in (401, 403):
                die(
                    f"LeetCode returned HTTP {exc.code}. "
                    "Your LEETCODE_SESSION/LEETCODE_CSRF_TOKEN is probably expired."
                )
            if exc.code == 429 and attempt < MAX_RETRIES:
                delay = min(30, 2 ** attempt)
                print(f"Rate limited; retrying in {delay}s...")
                time.sleep(delay)
                continue
            raise
        except (URLError, TimeoutError) as exc:
            if attempt < MAX_RETRIES:
                delay = min(30, 2 ** attempt)
                print(f"Network error ({exc}); retrying in {delay}s...")
                time.sleep(delay)
                continue
            raise

    raise RuntimeError("LeetCode request failed after retries.")


SUBMISSIONS_QUERY = """
query SubmissionList($offset: Int!, $limit: Int!) {
  submissionList(offset: $offset, limit: $limit, questionSlug: null) {
    hasNext
    submissions {
      id
      lang
      timestamp
      statusDisplay
      runtime
      title
      memory
      titleSlug
    }
  }
}
"""

DETAIL_QUERY = """
query SubmissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    question {
      questionId
      title
      titleSlug
    }
  }
}
"""

QUESTION_QUERY = """
query QuestionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    content
  }
}
"""


def normalize_name(name):
    name = name.lower().strip()
    name = re.sub(r"\s+", "-", name)
    return re.sub(r"[^a-zA-Z0-9_-]", "", name)


def pad_problem_id(value):
    value = str(value)
    return value if len(value) > 4 else ("000" + value)[-4:]


def existing_solution(title, lang):
    ext = LANG_TO_EXTENSION.get(lang)
    if not ext or not SOLUTIONS.exists():
        return False

    suffix = "-" + normalize_name(title)
    filename = f"solution.{ext}"

    for directory in SOLUTIONS.iterdir():
        if directory.is_dir() and directory.name.endswith(suffix):
            if (directory / filename).exists():
                return True
    return False


def get_new_submissions():
    found = []
    offset = 0

    while True:
        print(f"Fetching LeetCode submissions: offset {offset}")
        data = graphql(SUBMISSIONS_QUERY, {"offset": offset, "limit": PAGE_SIZE})
        result = data.get("submissionList")

        if result is None or result.get("submissions") is None:
            die(
                "LeetCode returned no submission list. "
                "Your LEETCODE_SESSION is likely expired."
            )

        submissions = result["submissions"]
        for submission in submissions:
            if submission.get("statusDisplay") != "Accepted":
                continue
            lang = submission.get("lang")
            title = submission.get("title")
            if not lang or not title or lang not in LANG_TO_EXTENSION:
                continue
            if not existing_solution(title, lang):
                found.append(submission)

        if not result.get("hasNext") or not submissions:
            break

        offset += PAGE_SIZE
        time.sleep(1)

    # Newest first; keep only the latest accepted submission for each
    # problem/language pair during this run.
    found.sort(key=lambda x: int(x.get("timestamp", 0)), reverse=True)
    seen = set()
    unique = []
    for submission in found:
        key = (submission["titleSlug"], submission["lang"])
        if key in seen:
            continue
        seen.add(key)
        unique.append(submission)
    return unique


def get_details(submission):
    data = graphql(DETAIL_QUERY, {"submissionId": int(submission["id"])})
    details = data.get("submissionDetails")
    if not details or not details.get("code"):
        raise RuntimeError(
            f"Could not retrieve code for submission {submission['id']} ({submission['title']})."
        )
    question = details.get("question") or {}
    return details["code"], question


def get_question_content(title_slug):
    data = graphql(QUESTION_QUERY, {"titleSlug": title_slug})
    question = data.get("question")
    return question.get("content") if question else None


def write_submission(submission, code, question):
    question_id = question.get("questionId")
    title = question.get("title") or submission["title"]
    title_slug = question.get("titleSlug") or submission["titleSlug"]
    ext = LANG_TO_EXTENSION[submission["lang"]]

    if not question_id:
        raise RuntimeError(f"No question ID returned for {title}.")

    folder = SOLUTIONS / f"{pad_problem_id(question_id)}-{normalize_name(title)}"
    folder.mkdir(parents=True, exist_ok=True)

    solution_path = folder / f"solution.{ext}"
    readme_path = folder / "README.md"

    if solution_path.exists():
        print(f"Skipping existing solution: {solution_path.relative_to(ROOT)}")
        return False

    content = get_question_content(title_slug)
    if content:
        readme_path.write_text(content.rstrip() + "\n", encoding="utf-8")
    elif not readme_path.exists():
        readme_path.write_text(
            f"# {title}\n\nUnable to fetch the problem statement.\n",
            encoding="utf-8",
        )

    solution_path.write_text(code.rstrip() + "\n", encoding="utf-8")
    print(f"Synced: {folder.name}/{solution_path.name}")
    return True


def main():
    SOLUTIONS.mkdir(exist_ok=True)

    submissions = get_new_submissions()
    print(f"Accepted submissions needing sync: {len(submissions)}")

    synced = 0
    for submission in submissions:
        try:
            code, question = get_details(submission)
            if write_submission(submission, code, question):
                synced += 1
            time.sleep(1)
        except Exception as exc:
            print(
                f"WARNING: failed to sync {submission.get('title')} "
                f"(submission {submission.get('id')}): {exc}",
                file=sys.stderr,
            )

    print(f"Done. Newly synced solutions: {synced}")


if __name__ == "__main__":
    main()
