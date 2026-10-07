#!/usr/bin/env python3

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


# ============================================================
# Configuration
# ============================================================

GRAPHQL_URL = "https://leetcode.com/graphql/"

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS_DIR = ROOT / "leetcode-solutions"

PAGE_SIZE = 100
SUBMISSION_PAGE_SIZE = 20
REQUEST_DELAY = 0.5


# ============================================================
# GraphQL client
# ============================================================

def graphql(query, variables=None, operation_name=None):
    """
    Send an authenticated GraphQL request to LeetCode.
    """

    session = os.environ.get("LEETCODE_SESSION")
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN")

    if not session:
        raise RuntimeError(
            "LEETCODE_SESSION secret is missing."
        )

    if not csrf:
        print(
            "WARNING: LEETCODE_CSRF_TOKEN is missing. "
            "Continuing without it."
        )

    payload = {
        "query": query,
        "variables": variables or {},
    }

    if operation_name:
        payload["operationName"] = operation_name

    body = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        GRAPHQL_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
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
                f"csrftoken={csrf or ''}"
            ),
            "x-csrftoken": csrf or "",
        },
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=30,
        ) as response:

            response_body = response.read().decode("utf-8")

    except urllib.error.HTTPError as exc:

        response_body = exc.read().decode(
            "utf-8",
            errors="replace",
        )

        print(f"\nLeetCode HTTP {exc.code}")
        print(response_body[:5000])

        raise RuntimeError(
            f"LeetCode GraphQL request failed "
            f"with HTTP {exc.code}"
        ) from exc

    except urllib.error.URLError as exc:

        raise RuntimeError(
            f"Could not connect to LeetCode: {exc.reason}"
        ) from exc

    try:
        result = json.loads(response_body)

    except json.JSONDecodeError as exc:

        print(response_body[:5000])

        raise RuntimeError(
            "LeetCode returned invalid JSON."
        ) from exc

    if result.get("errors"):

        print("\nGraphQL errors:")
        print(
            json.dumps(
                result["errors"],
                indent=2,
            )
        )

        raise RuntimeError(
            "LeetCode GraphQL returned errors."
        )

    return result.get("data", {})


# ============================================================
# Authentication test
# ============================================================

USER_STATUS_QUERY = """
query {
    userStatus {
        isSignedIn
        username
    }
}
"""


def check_authentication():
    """
    Verify that the LeetCode session cookie is valid.
    """

    print("Checking LeetCode authentication...")

    data = graphql(
        USER_STATUS_QUERY,
        operation_name=None,
    )

    status = data.get("userStatus")

    if not status:
        raise RuntimeError(
            "LeetCode did not return userStatus."
        )

    signed_in = status.get("isSignedIn")
    username = status.get("username")

    if not signed_in:
        raise RuntimeError(
            "LeetCode session is not signed in. "
            "Your LEETCODE_SESSION cookie may be expired."
        )

    print(
        f"Authenticated as: {username}"
    )

    return username


# ============================================================
# Get solved problems
# ============================================================

USER_PROGRESS_QUERY = """
query userProgressQuestionList(
    $filters: UserProgressQuestionListInput
) {
    userProgressQuestionList(
        filters: $filters
    ) {
        totalNum

        questions {
            frontendId
            title
            titleSlug
            difficulty
            lastSubmittedAt

            topicTags {
                name
            }
        }
    }
}
"""


def get_solved_problems():
    """
    Fetch all solved problems for the authenticated user.
    """

    problems = []
    skip = 0

    while True:

        print(
            f"Fetching solved problems: "
            f"skip={skip}"
        )

        variables = {
            "filters": {
                "questionStatus": "SOLVED",
                "skip": skip,
                "limit": PAGE_SIZE,
            }
        }

        data = graphql(
            USER_PROGRESS_QUERY,
            variables,
            "userProgressQuestionList",
        )

        result = data.get(
            "userProgressQuestionList"
        )

        if not result:
            raise RuntimeError(
                "LeetCode returned no "
                "userProgressQuestionList."
            )

        batch = result.get(
            "questions",
            [],
        )

        total = result.get(
            "totalNum",
            0,
        )

        problems.extend(batch)

        print(
            f"  Received {len(batch)} "
            f"problems "
            f"({len(problems)}/{total})"
        )

        if not batch:
            break

        if len(problems) >= total:
            break

        skip += PAGE_SIZE

        time.sleep(REQUEST_DELAY)

    return problems


# ============================================================
# Get submissions for a problem
# ============================================================

SUBMISSION_LIST_QUERY = """
query submissionList(
    $offset: Int!
    $limit: Int!
    $questionSlug: String!
) {
    questionSubmissionList(
        offset: $offset
        limit: $limit
        questionSlug: $questionSlug
    ) {
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


def get_latest_accepted_submission(
    title_slug,
):
    """
    Get the newest Accepted submission
    for a particular problem.
    """

    data = graphql(
        SUBMISSION_LIST_QUERY,
        {
            "offset": 0,
            "limit": SUBMISSION_PAGE_SIZE,
            "questionSlug": title_slug,
        },
        "submissionList",
    )

    result = data.get(
        "questionSubmissionList"
    )

    if not result:
        return None

    submissions = result.get(
        "submissions",
        [],
    )

    for submission in submissions:

        if submission.get(
            "statusDisplay"
        ) == "Accepted":

            return submission

    return None


# ============================================================
# Submission details
# ============================================================

SUBMISSION_DETAILS_QUERY = """
query SubmissionDetails(
    $submissionId: Int!
) {
    submissionDetails(
        submissionId: $submissionId
    ) {
        code

        question {
            questionId
            questionFrontendId
            title
            titleSlug
        }
    }
}
"""


def get_submission_details(
    submission_id,
):
    """
    Fetch the actual source code.
    """

    data = graphql(
        SUBMISSION_DETAILS_QUERY,
        {
            "submissionId": int(
                submission_id
            ),
        },
        "SubmissionDetails",
    )

    return data.get(
        "submissionDetails"
    )


# ============================================================
# Question metadata
# ============================================================

QUESTION_QUERY = """
query QuestionData(
    $titleSlug: String!
) {
    question(
        titleSlug: $titleSlug
    ) {
        questionId
        questionFrontendId
        title
        titleSlug
        difficulty

        topicTags {
            name
            slug
        }
    }
}
"""


def get_question(title_slug):
    """
    Fetch problem metadata.
    """

    data = graphql(
        QUESTION_QUERY,
        {
            "titleSlug": title_slug,
        },
        "QuestionData",
    )

    return data.get(
        "question"
    )


# ============================================================
# File helpers
# ============================================================

LANGUAGE_EXTENSIONS = {
    "python": "py",
    "python3": "py",

    "cpp": "cpp",
    "c++": "cpp",

    "c": "c",

    "java": "java",

    "javascript": "js",
    "typescript": "ts",

    "kotlin": "kt",

    "swift": "swift",

    "go": "go",

    "rust": "rs",

    "ruby": "rb",

    "php": "php",

    "csharp": "cs",
    "c#": "cs",

    "scala": "scala",

    "dart": "dart",

    "shell": "sh",

    "mysql": "sql",
    "mssql": "sql",
    "oracle": "sql",
}


def normalize_title(title):
    """
    Convert problem title into a safe folder name.
    """

    title = title.lower()

    title = re.sub(
        r"[^a-z0-9]+",
        "-",
        title,
    )

    return title.strip("-")


def language_extension(language):
    """
    Convert LeetCode language into a file extension.
    """

    language = (
        language
        .lower()
        .strip()
    )

    return LANGUAGE_EXTENSIONS.get(
        language,
        "txt",
    )


def make_solution_directory(problem):
    """
    Create:

    leetcode-solutions/
        0001-two-sum/
    """

    frontend_id = str(
        problem.get(
            "frontendId",
            problem.get(
                "questionFrontendId",
                "0000",
            ),
        )
    )

    title = problem["title"]

    safe_id = frontend_id.zfill(4)

    safe_title = normalize_title(
        title
    )

    return (
        SOLUTIONS_DIR
        / f"{safe_id}-{safe_title}"
    )


def find_existing_solution(
    title_slug,
):
    """
    Check whether a problem is already
    present in the repository.
    """

    if not SOLUTIONS_DIR.exists():
        return False

    normalized = normalize_title(
        title_slug
    )

    for directory in SOLUTIONS_DIR.iterdir():

        if not directory.is_dir():
            continue

        directory_name = (
            directory.name.lower()
        )

        if normalized in directory_name:
            return True

    return False


# ============================================================
# Write solution
# ============================================================

def write_solution(
    problem,
    submission,
    details,
    question,
):
    """
    Write solution code and README.
    """

    solution_dir = (
        make_solution_directory(
            problem
        )
    )

    solution_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    language = submission.get(
        "lang",
        "text",
    )

    extension = language_extension(
        language
    )

    code = details.get(
        "code"
    )

    if not code:
        print(
            "  No source code returned."
        )

        return False

    solution_file = (
        solution_dir
        / f"solution.{extension}"
    )

    solution_file.write_text(
        code.rstrip() + "\n",
        encoding="utf-8",
    )

    topics = []

    for tag in question.get(
        "topicTags",
        [],
    ):

        name = tag.get(
            "name"
        )

        if name:
            topics.append(name)

    frontend_id = problem.get(
        "frontendId",
        problem.get(
            "questionFrontendId",
            "N/A",
        ),
    )

    difficulty = problem.get(
        "difficulty",
        "Unknown",
    )

    title_slug = problem[
        "titleSlug"
    ]

    readme = solution_dir / "README.md"

    content = f"""# {problem["title"]}

- **LeetCode:** https://leetcode.com/problems/{title_slug}/
- **Problem ID:** {frontend_id}
- **Difficulty:** {difficulty}
- **Language:** {language}
"""

    if topics:
        content += (
            "- **Topics:** "
            + ", ".join(topics)
            + "\n"
        )

    content += f"""
## Solution

See [`solution.{extension}`](./solution.{extension}).
"""

    readme.write_text(
        content,
        encoding="utf-8",
    )

    print(
        f"  Saved: {solution_dir}"
    )

    return True


# ============================================================
# Main
# ============================================================

def main():

    print("=" * 60)
    print("LeetCode Sync")
    print("=" * 60)

    if not os.environ.get(
        "LEETCODE_SESSION"
    ):
        print(
            "ERROR: "
            "LEETCODE_SESSION is missing."
        )

        sys.exit(1)

    SOLUTIONS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    # --------------------------------------------------------
    # 1. Authentication
    # --------------------------------------------------------

    try:

        username = check_authentication()

    except Exception as exc:

        print(
            f"\nAuthentication failed: {exc}"
        )

        sys.exit(1)

    print(
        f"\nStarting sync for @{username}"
    )

    # --------------------------------------------------------
    # 2. Get solved problems
    # --------------------------------------------------------

    print(
        "\n1. Getting solved problems..."
    )

    try:

        problems = get_solved_problems()

    except Exception as exc:

        print(
            f"\nFailed to get solved problems:"
        )

        print(exc)

        sys.exit(1)

    print(
        f"\nFound {len(problems)} solved problems."
    )

    if not problems:

        print(
            "No solved problems were returned."
        )

        sys.exit(0)

    # --------------------------------------------------------
    # 3. Sync
    # --------------------------------------------------------

    print(
        "\n2. Syncing solutions..."
    )

    created = 0
    skipped = 0
    failed = 0

    for index, problem in enumerate(
        problems,
        start=1,
    ):

        title = problem.get(
            "title",
            "Unknown",
        )

        slug = problem.get(
            "titleSlug"
        )

        frontend_id = problem.get(
            "frontendId",
            "?"
        )

        print(
            f"\n[{index}/{len(problems)}] "
            f"{frontend_id}. {title}"
        )

        if not slug:

            print(
                "  Missing titleSlug. "
                "Skipping."
            )

            failed += 1
            continue

        # ----------------------------------------------------
        # Skip existing
        # ----------------------------------------------------

        if find_existing_solution(
            slug
        ):

            print(
                "  Already exists. Skipping."
            )

            skipped += 1
            continue

        # ----------------------------------------------------
        # Get accepted submission
        # ----------------------------------------------------

        try:

            submission = (
                get_latest_accepted_submission(
                    slug
                )
            )

        except Exception as exc:

            print(
                f"  Could not fetch submission: "
                f"{exc}"
            )

            failed += 1
            continue

        if not submission:

            print(
                "  No Accepted submission found."
            )

            failed += 1
            continue

        print(
            "  Accepted submission: "
            f"{submission.get('id')} "
            f"({submission.get('lang')})"
        )

        time.sleep(
            REQUEST_DELAY
        )

        # ----------------------------------------------------
        # Get source code
        # ----------------------------------------------------

        try:

            details = (
                get_submission_details(
                    submission["id"]
                )
            )

        except Exception as exc:

            print(
                f"  Could not fetch code: "
                f"{exc}"
            )

            failed += 1
            continue

        if not details:

            print(
                "  No submission details returned."
            )

            failed += 1
            continue

        time.sleep(
            REQUEST_DELAY
        )

        # ----------------------------------------------------
        # Get question metadata
        # ----------------------------------------------------

        try:

            question = get_question(
                slug
            )

        except Exception as exc:

            print(
                f"  Could not fetch question "
                f"metadata: {exc}"
            )

            failed += 1
            continue

        if not question:

            print(
                "  Question metadata missing."
            )

            failed += 1
            continue

        # ----------------------------------------------------
        # Write files
        # ----------------------------------------------------

        try:

            success = write_solution(
                problem,
                submission,
                details,
                question,
            )

            if success:
                created += 1
            else:
                failed += 1

        except Exception as exc:

            print(
                f"  Failed to write solution: "
                f"{exc}"
            )

            failed += 1

        time.sleep(
            REQUEST_DELAY
        )

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("Sync complete")
    print("=" * 60)

    print(
        f"New solutions : {created}"
    )

    print(
        f"Skipped       : {skipped}"
    )

    print(
        f"Failed        : {failed}"
    )

    print(
        f"Total solved  : {len(problems)}"
    )

    print("=" * 60)


if __name__ == "__main__":
    main()
