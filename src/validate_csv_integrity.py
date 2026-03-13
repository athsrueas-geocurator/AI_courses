#!/usr/bin/env python3
import csv
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
COURSES_CSV = ROOT / "courses.csv"
LESSONS_CSV = ROOT / "lessons.csv"


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def fail(message: str):
    print(f"ERROR: {message}")


def main() -> int:
    errors = []

    courses = read_csv(COURSES_CSV)
    lessons = read_csv(LESSONS_CSV)

    if not courses:
        errors.append("courses.csv has no rows")
    if not lessons:
        errors.append("lessons.csv has no rows")

    required_course_fields = [
        "Course ID",
        "Name",
        "Description",
        "Providers",
        "Web URL",
        "Topics",
        "Skills",
        "Roles",
    ]
    required_lesson_fields = [
        "Name",
        "Description",
        "Stages",
        "Topics",
        "Lesson number",
        "Courses",
        "Skills",
        "Roles",
        "Web URL",
    ]

    course_ids = set()
    for idx, row in enumerate(courses, start=2):
        for field in required_course_fields:
            if not row.get(field, "").strip():
                errors.append(f"courses.csv:{idx} missing required field '{field}'")

        course_id = row.get("Course ID", "").strip()
        if course_id:
            if course_id in course_ids:
                errors.append(f"courses.csv:{idx} duplicate Course ID '{course_id}'")
            course_ids.add(course_id)

        url = row.get("Web URL", "").strip()
        if url and not is_valid_url(url):
            errors.append(f"courses.csv:{idx} invalid URL format '{url}'")

    seen_lesson_keys = set()
    for idx, row in enumerate(lessons, start=2):
        for field in required_lesson_fields:
            if not row.get(field, "").strip():
                errors.append(f"lessons.csv:{idx} missing required field '{field}'")

        lesson_key = (row.get("Courses", "").strip(), row.get("Lesson number", "").strip())
        if all(lesson_key):
            if lesson_key in seen_lesson_keys:
                errors.append(
                    f"lessons.csv:{idx} duplicate (Courses, Lesson number) {lesson_key}"
                )
            seen_lesson_keys.add(lesson_key)

        course_ref = row.get("Courses", "").strip()
        if course_ref and course_ref not in course_ids:
            errors.append(
                f"lessons.csv:{idx} references unknown Course ID '{course_ref}'"
            )

        url = row.get("Web URL", "").strip()
        if url and not is_valid_url(url):
            errors.append(f"lessons.csv:{idx} invalid URL format '{url}'")

    if errors:
        for err in errors:
            fail(err)
        print(f"\nValidation failed with {len(errors)} issue(s).")
        return 1

    print("Validation passed: course/lesson links, uniqueness, required fields, and URL format are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
