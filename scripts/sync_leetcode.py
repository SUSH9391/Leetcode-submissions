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
OUTPUT_DIR = Path("leetcode-solutions")

PAGE_SIZE = 100


# ---------------------------------------------------------------------
# HTTP / GraphQL
# ---------------------------------------------------------------------

def graphql(query, variables, operation_name):
    session = os.environ.get("LEETCODE_SESSION")
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN")

    if not session:
        raise RuntimeError("LEETCODE_SESSION secret is missing.")

    if not csrf:
        raise RuntimeError("LEETCODE_CSRF_TOKEN secret is missing.")

    data = json.dumps({
        "operationName": operation_name,
        "variables": variables,
        "query": query,
    }).encode("utf-8")

    request = urllib.request.Request(
        GRAPHQL_URL,
        data=data,
        headers={
            "Content-Type": "application/json",
            "Origin": "https://leetcode.com",
            "Referer": "https://leetcode.com/",
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/154.0.0.0 Safari/537.36"
            ),
            "Cookie": (
                f"LEETCODE_SESSION={session}; "
                f"csrftoken={csrf}"
            ),
            "x-csrftoken": csrf,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")

    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")

        print(
            f"LeetCode HTTP {error.code} for {operation_name}",
            file=sys.stderr,
        )
        print(body[:2000], file=sys.stderr)

        raise

    except urllib.error.URLError as error:
        raise RuntimeError(
            f"Could not connect to LeetCode: {error}"
        ) from error

    try:
        payload = json.loads(body)
    except json.JSONDecodeError as error:
        print(body[:2000], file=sys.stderr)
        raise RuntimeError("LeetCode returned invalid JSON.") from error

    if payload.get("errors"):
        print(
            json.dumps(payload["errors"], indent=2),
            file=sys.stderr,
        )
        raise RuntimeError(
            f"LeetCode GraphQL query failed: {operation_name}"
        )

    if "data" not in payload:
        raise RuntimeError(
            f"LeetCode response contained no data: {payload}"
        )

    return payload["data"]


# ---------------------------------------------------------------------
# Queries
# ---------------------------------------------------------------------

USER_PROFILE_QUESTIONS_QUERY = """
query UserProfileQuestions(
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
            runtime
            memory
            title
            titleSlug
        }
    }
}
"""


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


QUESTION_QUERY = """
query QuestionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        titleSlug
        difficulty
        content
    }
}
"""


# ---------------------------------------------------------------------
# LeetCode API
# ---------------------------------------------------------------------

def get_accepted_problems():
    print("Fetching accepted LeetCode problems...")

    all_questions = []
    skip = 0

    while True:
        data = graphql(
            USER_PROFILE_QUESTIONS_QUERY,
            {
                "status": "ACCEPTED",
                "skip": skip,
                "first": PAGE_SIZE,
                "sortField": "LAST_SUBMITTED_AT",
                "sortOrder": "DESCENDING",
            },
            "UserProfileQuestions",
        )

        result = data["userProfileQuestions"]

        questions = result.get("questions", [])

        if not questions:
            break

        all_questions.extend(questions)

        total = result.get("totalNum", len(all_questions))

        print(
            f"  Found {len(all_questions)}/{total} accepted problems"
        )

        skip += len(questions)

        if skip >= total:
            break

        time.sleep(0.2)

    return all_questions


def get_latest_accepted_submission(question_slug):
    """
    Get the latest accepted submission for one problem.
    """

    offset = 0
    last_key = None

    while True:
        data = graphql(
            SUBMISSIONS_QUERY,
            {
                "offset": offset,
                "limit": 20,
                "lastKey": last_key,
                "questionSlug": question_slug,
            },
            "Submissions",
        )

        result = data["submissionList"]

        submissions = result.get("submissions", [])

        for submission in submissions:
            if submission.get("statusDisplay") == "Accepted":
                return submission

        if not result.get("hasNext"):
            break

        last_key = result.get("lastKey")
        offset += len(submissions)

        time.sleep(0.2)

    return None


def get_submission_code(submission_id):
    data = graphql(
        SUBMISSION_DETAILS_QUERY,
        {
            "submissionId": int(submission_id),
        },
        "SubmissionDetails",
    )

    result = data.get("submissionDetails")

    if not result:
        return None

    return result.get("code")


def get_question(question_slug):
    data = graphql(
        QUESTION_QUERY,
        {
            "titleSlug": question_slug,
        },
        "QuestionData",
    )

    return data.get("question")


# ---------------------------------------------------------------------
# Local repository helpers
# ---------------------------------------------------------------------

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
    "ruby": "rb",
    "php": "php",
    "scala": "scala",
    "dart": "dart",
    "sql": "sql",
}


def normalize_name(value):
    value = value.lower()

    value = re.sub(
        r"[^a-z0-9]+",
        "-",
        value,
    )

    value = value.strip("-")

    return value


def language_extension(language):
    language = language.lower().strip()

    return LANGUAGE_EXTENSIONS.get(
        language,
        normalize_name(language) or "txt",
    )


def existing_solution(slug):
    """
    Check whether this problem already exists in the repository.
    """

    if not OUTPUT_DIR.exists():
        return False

    for directory in OUTPUT_DIR.iterdir():

        if not directory.is_dir():
            continue

        if slug in directory.name.lower():
            return True

        metadata_file = directory / "metadata.json"

        if metadata_file.exists():
            try:
                metadata = json.loads(
                    metadata_file.read_text(
                        encoding="utf-8"
                    )
                )

                if metadata.get("titleSlug") == slug:
                    return True

            except Exception:
                pass

    return False


def find_existing_by_slug(slug):
    if not OUTPUT_DIR.exists():
        return None

    for directory in OUTPUT_DIR.iterdir():

        if not directory.is_dir():
            continue

        metadata_file = directory / "metadata.json"

        if not metadata_file.exists():
            continue

        try:
            metadata = json.loads(
                metadata_file.read_text(
                    encoding="utf-8"
                )
            )

            if metadata.get("titleSlug") == slug:
                return directory

        except Exception:
            continue

    return None


# ---------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------

def clean_html(html):
    if not html:
        return ""

    html = re.sub(
        r"<script.*?</script>",
        "",
        html,
        flags=re.S | re.I,
    )

    html = re.sub(
        r"<style.*?</style>",
        "",
        html,
        flags=re.S | re.I,
    )

    html = re.sub(
        r"<[^>]+>",
        "",
        html,
    )

    html = html.replace("&nbsp;", " ")
    html = html.replace("&lt;", "<")
    html = html.replace("&gt;", ">")
    html = html.replace("&amp;", "&")
    html = html.replace("&quot;", '"')

    return html.strip()


def create_readme(question, submission, code, extension):
    title = question.get(
        "title",
        submission.get("title", "LeetCode Problem"),
    )

    difficulty = question.get(
        "difficulty",
        "Unknown",
    )

    frontend_id = question.get(
        "questionFrontendId",
        "",
    )

    slug = question.get(
        "titleSlug",
        submission.get("titleSlug", ""),
    )

    content = clean_html(
        question.get("content", "")
    )

    language = submission.get(
        "lang",
        "Unknown",
    )

    return f"""# {frontend_id}. {title}

**Difficulty:** {difficulty}  
**Language:** {language}  
**LeetCode:** https://leetcode.com/problems/{slug}/

## Problem

{content}

## Solution

```{extension}
{code}
