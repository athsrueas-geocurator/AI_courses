# Row verification report (root CSVs)

Date: 2026-03-14

## Scope

- `courses.csv` (root): 3 rows
- `lessons.csv` (root): 44 rows
- Total verified rows: 47

## Method

1. Checked each `Web URL` for availability.
2. For GitHub lesson links, used raw-content equivalents during audit to avoid transient GitHub UI rate limits.
3. Verified each row's `Name` matched page content (title/body token match).
4. Verified each row's `Description` intent matched page content.
5. Applied Geo naming style guidelines to root CSV `Name` fields and synced `courses.csv` `Lessons` names accordingly.

## Results

- URL availability: 47/47 reachable
- Content alignment (`Name` + description intent): 47/47 matched
- Broken URLs requiring replacement via Brave search in this pass: 0

## Notes

- Previous Anthropic URL corrections remain valid and reachable:
  - `claude-with-the-anthropic-api`
  - `claude-with-google-vertex`
  - `claude-in-amazon-bedrock`

- Detailed machine-readable audit output files:
  - `url_content_audit.json`
  - `row_verification_report.json`
