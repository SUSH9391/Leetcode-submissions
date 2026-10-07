#!/usr/bin/env python3

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


GRAPHQL_URL = "https://leetcode.com/graphql"
ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS_DIR = ROOT / "leetcode-solutions"

PAGE_SIZE = 100
REQUEST_DELAY = 0.5


def graphql(query, variables, operation_name):
    session_cookie = os.environ.get("LEETCODE_SESSION")
    csrf_token = os.environ.get("LEETCODE_CSRF_TOKEN")

    if not session_cookie:
        raise RuntimeError("LEETCODE_SESSION secret is missing.")

    payload = json.dumps({
        "operationName": operation_name,
        "variables": variables,
        "query": query,
    }).encode("utf-8")

    request = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Origin": "https://leetcode.com",
            "Referer": "https://leetcode.com/",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/154.0.0.0 Safari/537.36"
            ),
            "Cookie": (
                f"LEETCODE_SESSION={session_cookie}; "
                f"csrftoken={csrf_token or ''}"
            ),
            "x-csrftoken": csrf_token or "",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")

    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")

        print(f"LeetCode HTTP {exc.code}")
        print(body[:2000])

        raise RuntimeError(
            f"LeetCode GraphQL request failed with HTTP {exc.code}"
        ) from exc

    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Could not connect to LeetCode: {exc.reason}"
        ) from exc

    try:
        result = json.loads(body)
    except json.JSONDecodeError as exc:
        print(body[:2000])
        raise RuntimeError("LeetCode returned invalid JSON.") from exc

    if result.get("errors"):
        print(json.dumps(result["errors"], indent=2))
        raise RuntimeError("LeetCode GraphQL returned errors.")

    return result.get("data", {})


# ---------------------------------------------------------------------------
# Get all problems the user has solved
# ---------------------------------------------------------------------------

USER_PROFILE_QUESTIONS_QUERY = """
query userProfileQuestions(
    $status: StatusFilterEnum!
    $skip: Int!
    $first: Int!
    $sortField: SortFieldEnum!
    $sortOrder: SortingOrderEnum!
) {
    userProfileQuestions(
        status: $status
        skip: $skip
        first: $first
        sortField: $sortField
        sortOrder: $sortOrder
    ) {
        totalNum
        questions {
            questionFrontendId
            title
            titleSlug
            difficulty
            lastSubmittedAt
        }
    }
}
"""


def get_accepted_problems():
    problems = []
    skip = 0

    while True:
        print(f"Fetching accepted problems: {skip}")

        data = graphql(
            USER_PROFILE_QUESTIONS_QUERY,
            {
                "status": "ACCEPTED",
                "skip": skip,
                "first": PAGE_SIZE,
                "sortField": "LAST_SUBMITTED_AT",
                "sortOrder": "DESCENDING",
            },
            "userProfileQuestions",
        )

        result = data.get("userProfileQuestions")

        if not result:
            raise RuntimeError(
                "LeetCode did not return userProfileQuestions."
            )

        batch = result.get("questions", [])
        total = result.get("totalNum", 0)

        problems.extend(batch)

        print(
            f"  received {len(batch)} problems "
            f"({len(problems)}/{total})"
        )

        if not batch or len(problems) >= total:
            break

        skip += PAGE_SIZE
        time.sleep(REQUEST_DELAY)

    return problems


# ---------------------------------------------------------------------------
# Get submissions for ONE problem
# ---------------------------------------------------------------------------

SUBMISSIONS_QUERY = """
query Submissions(
    $offset: Int!
    $limit: Int!
    $lastKey: String
    $questionSlug: String!
) {
    submissionList(
        offset: $offset
        limit: $limit
        lastKey: $lastKey
        questionSlug: $questionSlug
    ) {
        lastKey
        hasNext
        submissions {
            id
            statusDisplay
            lang
            timestamp
            title
            titleSlug
        }
    }
}
"""


def get_latest_accepted_submission(title_slug):
    data = graphql(
        SUBMISSIONS_QUERY,
        {
            "offset": 0,
            "limit": 20,
            "lastKey": None,
            "questionSlug": title_slug,
        },
        "Submissions",
    )

    result = data.get("submissionList")

    if not result:
        return None

    submissions = result.get("submissions", [])

    for submission in submissions:
        if submission.get("statusDisplay") == "Accepted":
            return submission

    return None


# ---------------------------------------------------------------------------
# Get submission source code
# ---------------------------------------------------------------------------

SUBMISSION_DETAILS_QUERY = """
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


def get_submission_details(submission_id):
    data = graphql(
        SUBMISSION_DETAILS_QUERY,
        {
            "submissionId": int(submission_id),
        },
        "SubmissionDetails",
    )

    return data.get("submissionDetails")


# ---------------------------------------------------------------------------
# Get question metadata
# ---------------------------------------------------------------------------

QUESTION_QUERY = """
query QuestionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        difficulty
        content
        topicTags {
            name
            slug
        }
    }
}
"""


def get_question(title_slug):
    data = graphql(
        QUESTION_QUERY,
        {
            "titleSlug": title_slug,
        },
        "QuestionData",
    )

    return data.get("question")


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

LANGUAGE_EXTENSIONS = {
    "python": "py",
    "python3": "py",
    "cpp": "cpp",
    "c++": "cpp",
    "java": "java",
    "javascript": "js",
    "typescript": "ts",
    "kotlin": "kt",
    "swift": "swift",
    "go": "go",
    "rust": "rs",
    "c": "c",
    "csharp": "cs",
    "c#": "cs",
    "php": "php",
}


def normalize_title(title):
    title = title.lower()

    title = re.sub(r"[^a-z0-9]+", "-", title)
    title = title.strip("-")

    return title


def language_extension(language):
    language = language.lower().strip()

    return LANGUAGE_EXTENSIONS.get(language, "txt")


def find_existing_solution(title_slug):
    if not SOLUTIONS_DIR.exists():
        return True

    normalized_slug = normalize_title(title_slug)

    for directory in SOLUTIONS_DIR.iterdir():
        if not directory.is_dir():
            continue

        if normalized_slug in directory.name.lower():
            return True

        if directory.name.lower().endswith(f"-{normalized_slug}"):
            return True

    return False


def make_solution_directory(problem):
    question_id = problem.get("questionFrontendId", "0000")
    title = problem["title"]

    safe_id = str(question_id).zfill(4)
    safe_title = normalize_title(title)

    return SOLUTIONS_DIR / f"{safe_id}-{safe_title}"


# ---------------------------------------------------------------------------
# Write solution
# ---------------------------------------------------------------------------

def write_solution(problem, submission, details, question):
    solution_dir = make_solution_directory(problem)

    solution_dir.mkdir(parents=True, exist_ok=True)

    language = submission.get("lang", "text")
    extension = language_extension(language)

    code = details.get("code")

    if not code:
        print("  No source code returned.")
        return False

    solution_file = solution_dir / f"solution.{extension}"

    solution_file.write_text(
        code.rstrip() + "\n",
        encoding="utf-8",
    )

    topic_tags = question.get("topicTags", [])

    topics = [
        tag.get("name")
        for tag in topic_tags
        if tag.get("name")
    ]

    readme = solution_dir / "README.md"

    readme_content = f"""# {problem["title"]}

- **LeetCode:** https://leetcode.com/problems/{problem["titleSlug"]}/
- **Problem ID:** {problem["questionFrontendId"]}
- **Difficulty:** {problem["difficulty"]}
- **Language:** {language}
"""

    if topics:
        readme_content += (
            "- **Topics:** "
            + ", ".join(topics)
            + "\n"
        )

    readme_content += "\n## Solution\n\n"
    readme_content += f"See [`solution.{extension}`](./solution.{extension}).\n"

    readme.write_text(
        readme_content,
        encoding="utf-8",
    )

    print(f"  Saved: {solution_dir}")

    return True


# ---------------------------------------------------------------------------
# Main sync process
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("LeetCode Sync")
    print("=" * 60)

    if not os.environ.get("LEETCODE_SESSION"):
        print("ERROR: LEETCODE_SESSION is not configured.")
        sys.exit(1)

    SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)

    print("\n1. Getting accepted problems...")
    problems = get_accepted_problems()

    print(f"\nFound {len(problems)} accepted problems.")

    if not problems:
        print("No accepted problems found.")
        return

    created = 0
    skipped = 0
    failed = 0

    print("\n2. Syncing solutions...")

    for index, problem in enumerate(problems, start=1):
        title = problem["title"]
        slug = problem["titleSlug"]

        print(
            f"\n[{index}/{len(problems)}] "
            f"{problem['questionFrontendId']}. {title}"
        )

        if find_existing_solution(slug):
            print("  Already exists. Skipping.")
            skipped += 1
            continue

        try:
            submission = get_latest_accepted_submission(slug)

            if not submission:
                print("  No accepted submission found.")
                failed += 1
                continue

            print(
                f"  Accepted submission: "
                f"{submission['id']} "
                f"({submission['lang']})"
            )

            time.sleep(REQUEST_DELAY)

            details = get_submission_details(
                submission["id"]
            )

            if not details:
                print("  Could not get submission details.")
                failed += 1
                continue

            time.sleep(REQUEST_DELAY)

            question = get_question(slug)

            if not question:
                print("  Could not get question metadata.")
                failed += 1
                continue

            if write_solution(
                problem,
                submission,
                details,
                question,
            ):
                created += 1
            else:
                failed += 1

            time.sleep(REQUEST_DELAY)

        except Exception as exc:
            print(f"  ERROR: {exc}")
            failed += 1

    print("\n" + "=" * 60)
    print("Sync complete")
    print("=" * 60)

    print(f"New solutions : {created}")
    print(f"Skipped       : {skipped}")
    print(f"Failed        : {failed}")

    if failed:
        print(
            "\nSome problems could not be synced. "
            "The workflow will still finish."
        )


if __name__ == "__main__":
    main()
