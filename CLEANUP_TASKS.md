# AI Courses Data Cleanup Tasks

Purpose: track dataset cleanup work across sessions for `courses.csv` and `lessons.csv`.

## Current status

- Last URL audit: 2026-03-13
- URL checks run across all `Web URL` values in both CSV files
- Broken URLs found: 1
- Broken URLs fixed: 1 (`lessons.csv` Phoenix docs index row)

## Task checklist

## URL verification task (row-by-row)

- [x] Verify every row in root `courses.csv` against live page content.
- [x] Verify every row in root `lessons.csv` against live page content.
- [x] Confirm all URLs resolve (HTTP 200) using direct fetch or GitHub raw fallback for rate-limited pages.
- [x] Confirm page content matches row `Name` and `Description` intent before accepting URL.
- [x] Apply Geo style guide naming/description format rules to root CSV rows.

### Broken URL fix rule (mandatory)

- If a URL fails, use Brave search to find a very similar candidate URL on the same source domain.
- Suggested query format:
  - `"<row Name>" "<provider or course>" site:<expected-domain>`
- Accept replacement only when both are true:
  - URL is reachable.
  - Page content matches the row metadata (`Name`, `Description`, and source context).

## User-requested roadmap (source of truth)

### 1. Add stable course key in courses.csv

- [x] Add a new `Course ID` column (slug format) to `courses.csv:1`.
- [x] Populate all 16 rows with IDs that match `lessons.csv` `Courses` values.
- [x] Keep `Name` human-readable; use `Course ID` for joins.

### 2. Backfill explicit course mapping (deterministic)

- [x] Use this inferred mapping as the source of truth:
  - `azure-llmops-workshop` -> `LLMOps Workshop (Azure)`
  - `gcp-llmops-overview` -> `LLMOps on Google Cloud`
  - `aws-llmops-workshop` -> `LLMOps Workshop (SageMaker open LLM)`
  - `aws-llmops-blog-series` -> `Operationalize GenAI Apps with LLMOps (blog series)`
  - `databricks-llmops` -> `LLMOps on Databricks`
  - `ibm-llmops` -> `LLMOps (IBM Think)`
  - `oracle-llmops` -> `LLMOps (Oracle)`
  - `hf-open-llmops-primitives` -> `Open LLMOps Primitives (HF ecosystem)`
  - `eleutherai-eval` -> `LLMOps Evaluation Harness`
  - `vllm-serving` -> `vLLM Serving & OpenAI-Compatible API`
  - `phoenix-observability` -> `Phoenix Observability & Evals`
  - `mlflow-genai` -> `MLflow for GenAI (Prompt Registry + Eval)`
  - `openrlhf-posttraining` -> `OpenRLHF (RLHF pipelines)`
  - `langchain-observability` -> `LangChain Observability (OSS)`
  - `llamaindex-observability` -> `LlamaIndex Observability (OSS)`
  - `openclaw-getting-started` -> `OpenClaw Getting Started`

### 3. Fill currently empty high-value columns

- [x] `courses.csv`: backfill `Lessons` (list lesson names or IDs), `Goals` (2-4 outcomes/course), and `Tags` (5-8 normalized tags).
- [x] `lessons.csv`: backfill `Stages` for all rows; either fill or intentionally deprecate `Related spaces`.
- [x] `Related spaces` policy finalized: keep column and populate consistently (do not leave mostly empty).

### 4. Normalize controlled vocabularies

- [ ] Standardize role names (`Platform engineer` vs `Platform Engineer`, `Governance manager` vs `Governance lead`, etc.).
- [ ] Standardize topic labels (`Evaluation and Testing` vs close variants) and tag casing.
- [ ] Define a short taxonomy doc (or README section) with allowed values.

### 5. Fix quality outliers

- [ ] Replace placeholder descriptions like `Lesson on ...` with concrete summaries.
- [x] Fix suspicious URL at `lessons.csv:65` (was truncated; now fixed).
- [x] Ensure every lesson has non-empty `Description`, `Stages`, `Topics`, `Skills`, `Roles`, `Web URL`.

### 6. Add integrity checks (scripted)

- [x] Validate every `lessons.csv` `Courses` value exists in `courses.csv` `Course ID`.
- [x] Validate uniqueness of `(Course ID, Lesson number)` in lessons.
- [x] Validate required non-empty fields and URL format; fail fast on violations.

### Execution order

- [x] Pass 1: schema/link normalization (`Course ID`, joins, validations)
- [ ] Pass 2: content backfill + taxonomy cleanup

### 1) Schema and join integrity

- [ ] Add `Course ID` column to `courses.csv` (slug format)
- [ ] Populate all `Course ID` values to match `lessons.csv` `Courses`
- [ ] Add validation script: every `lessons.csv` `Courses` value must exist in `courses.csv` `Course ID`
- [ ] Add validation script: enforce unique `(Courses, Lesson number)` pairs

### 2) Completeness backfill

- [x] Backfill `courses.csv` `Lessons` column
- [x] Backfill `courses.csv` `Goals` column (2-4 outcomes per course)
- [x] Decide `Related spaces` policy (populate or remove) and apply consistently to both files
- [ ] Backfill `lessons.csv` `Stages` for all rows

### 3) Taxonomy normalization

- [ ] Normalize role labels (title/casing and canonical names)
- [ ] Normalize topic labels to a controlled list
- [ ] Normalize tags formatting and casing
- [ ] Add a short taxonomy reference section to `README.md` (or create `DATA_TAXONOMY.md`)

### 4) Content quality

- [ ] Replace placeholder descriptions that start with `Lesson on ...`
- [ ] Review course and lesson descriptions for consistency and specificity
- [ ] Confirm each lesson has non-empty `Description`, `Topics`, `Skills`, `Roles`, and valid `Web URL`

### 5) URL health maintenance

- [ ] Add reusable URL checker script (or documented one-liner)
- [ ] Run URL audit before each release/update
- [ ] For any failed URL: resolve via Brave Search and update source CSV

## Notes from latest audit

- Updated URL in `lessons.csv` for `Phoenix docs section index (tracing/evals/datasets)`:
  - Old: `https://docs.arize.com/phoenix/tracing/how-to-tracing/trace-`
  - New: `https://arize.com/docs/phoenix`

## Validation run notes

- Added validator script: `src/validate_csv_integrity.py`
- Latest run: pass (`python src/validate_csv_integrity.py`)
- Course join integrity is now wired through `Course ID` and validated
- `Stages` now backfilled for all rows using topic-derived stage labels

## Related spaces notes

- Queried Geo API testnet and identified candidate DAO spaces by page name:
  - `AI` (`41e851610e13a19441c4d980f2f2ce6b`)
  - `Technology` (`870e3b3068661e6280fad2ab456829bc`)
  - `Geo Education` (`784bfddae3f3976118c561bf28195b44`)
- Applied current policy: set `Related spaces=AI` for all courses and lessons (kept existing values where already `AI`).
- Tool-level Geo helper issues are logged in `geo_api_errors.md`.

## Course field backfill notes

- Backfilled `courses.csv` `Lessons` from `lessons.csv` grouped by `Courses` and ordered by `Lesson number`.
- Backfilled `courses.csv` `Goals` with 3 outcome statements per course.
- Backfilled `courses.csv` `Tags` with normalized 5-8 tag sets per course.
- Post-backfill integrity check passed: `python src/validate_csv_integrity.py`.

## Geo style guide source of truth

- Source of truth: https://www.geobrowser.io/space/3be38bb922bc80c6a6503fbbba28d2b0/dd5546417d00442fb353c7b10f8b7163
- Always check every URL before publishing; replace broken or outdated links with working canonical URLs.
