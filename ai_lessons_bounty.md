# Geo AI Courses & Lessons Bounty — LLMOps Catalog Plan

## What We’re Doing

We’re building a **high-quality, browsable learning catalog for LLMOps** inside Geo.

The output will be a set of structured **Course** and **Lesson** entities, connected to **Topic** and **Person** entities, so learners can navigate “what to learn next” and see how concepts relate across ecosystems.

---

## Why LLMOps

LLMOps is the widely used umbrella for **operationalizing LLM systems end-to-end**:

**prompt + data → evaluation → deployment → monitoring → iteration**,
with production concerns like **cost, latency, reliability, and governance**.

This aligns strongly with Mozilla’s “open ecosystem” thesis: LLMOps is where open tooling, evaluation, and serving standards become practical.

---

## How We’re Attacking It

We’ll curate LLMOps using a **two-pronged, consensus-driven approach**:

### 1) Cloud Platform “Courses”

Treat each major cloud platform’s official guidance/workshops as a Course
(Azure, AWS, GCP, Databricks, IBM, Oracle).

These provide the enterprise-standard view of lifecycle, deployment patterns, and governance.

### 2) Open-Source “Courses”

Treat major OSS communities/tools as Courses
(Hugging Face/TRL, EleutherAI eval harness, vLLM serving, Phoenix observability, MLflow, OpenRLHF, LangChain, LlamaIndex).

These provide the practical “open ecosystem primitives” view: eval harnesses, serving engines, tracing, post-training pipelines.

Together, these two lenses create a reliable “consensus map” of what LLMOps includes.

---

## What We’re Publishing (Structure)

We will produce:

* **Courses**: one per platform/community/toolset (14 total in the current draft)
* **Lessons**: key modules/pages/labs within each course (each with title, short description, URL, and order)
* **Topics**: a consistent LLMOps topic taxonomy
* **People**: instructors/authors/maintainers when clearly attributable

---

## LLMOps Topic Map (Tags)

Each Course/Lesson will be tagged with a shared topic vocabulary:

* Lifecycle
* Prompt management
* Evaluation
* Observability & tracing
* Deployment & serving
* Post-training (SFT / PEFT / RLHF / DPO)
* Governance & risk
* Cost & performance

---

## Quality and Ranking Principles

We will rank and select material using these rules:

1. **Primary sources first** (official docs, workshops, canonical repos)
2. **Runnable > slide-only** (hands-on labs and reproducible examples)
3. **Evaluation + observability are required** (not optional add-ons)
4. **Vendor-neutral concepts first**, vendor-specific implementations second
5. Prefer sources that show **versioning and experiments** (prompts, datasets, model artifacts)

---

## Deliverable Format (Simple + Ingestible)

We’re working **offline** in a simple table format (Sheets / CSV):

* `courses` table
* `lessons` table (every lesson has a URL)
* Optional: `topics` and `people` tables

This keeps authoring fast, reviewable, and easy to upload into Geo with clean relationships.

---

## Current Status

* Topic selected: **LLMOps**
* Initial catalog assembled: **14 Courses** (6 cloud + 8 open-source)
* Lesson URLs: included for each course in the working dataset
* Next step: expand lesson coverage where needed, normalize IDs/tags, and fill short descriptions consistently