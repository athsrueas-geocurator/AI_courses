# LLMOps Courses & Lessons (Geo Bounty Draft)

## What this is
I’m **Thomas Freestone** and I’m compiling a curated list of **LLMOps learning resources** for Geo.  
I’m using AI to help brainstorm, structure, and format the list, but **I’m personally responsible for reviewing and finalizing what gets included**.

## Goal
Turn the best public LLMOps material into a Geo-friendly catalog of:
- **Courses** (major platforms/communities/tools)
- **Lessons** (units within each course, ordered)
- **Topic tags** (LLMOps taxonomy)
- Optional **People** (authors/instructors/maintainers when clearly attributable)

## Current status (initial draft only)
Right now this repo contains **only an initial draft list**:
- a first pass at “what should count as a Course”
- an initial set of Lesson URLs per Course

This is **not audited yet**, and some links may not be the best entry point for a learner.

## Next steps (manual audit plan)
I will manually audit and refine the list by:
1) **Verifying every link**
   - ensure it loads correctly and is stable
   - replace fragile/over-specific links with better entry points when needed

2) **Selecting the best entry point for each lesson**
   - prefer “Getting Started” / overview pages before deep technical references
   - prefer canonical docs/labs over random mirrors or secondary blog posts

3) **Normalizing structure**
   - stable IDs (`course_id`, `lesson_id`)
   - consistent lesson ordering (`lesson_num`)
   - consistent topic tags across all courses/lessons

4) **Removing weak/duplicate items**
   - keep only widely recognized, high-quality material
   - reduce redundancy across courses where it doesn’t add learning value

## Link selection rules (what I’m aiming for)
When multiple URLs exist, I will prefer links that are:
- **Official/canonical**
- **Stable**
- **Beginner-appropriate as an entry point**
- **Actionable** (docs/labs with clear steps)

## Geo publisher CSV rules (important)

The publisher expects these files and columns:

- `courses.csv`: `Course ID`, `Name`, `Description`, `Providers`, `Web URL`, `Related spaces`, `Topics`, `Skills`, `Roles`, `Tags`, `Lessons`, `Goals`
- `lessons.csv`: `Name`, `Description`, `Stages`, `Topics`, `Lesson number`, `Courses`, `Related spaces`, `Skills`, `Tags`, `Roles`, `Web URL`

### Fields used only for linking (not published as values)

- `Course ID` is a source key for cross-file linking.
- Geo entity IDs are generated at publish time; do not try to prefill them in CSV.

### Course -> Lesson linking behavior

`courses.csv` `Lessons` is converted into relations to lesson entities.

Supported token formats:
- semicolon-separated lesson references
- exact lesson names
- numbered references like `1. Lesson name; 2. Lesson name`

The publisher strips list ordinals (`^\d+\.`) and matches intelligently against:
- existing lesson entities in the target space
- lesson entities being created in the same publish run

### Lesson -> Course linking behavior

`lessons.csv` `Courses` must contain `Course ID` values from `courses.csv`.

Example:
- `lessons.csv` `Courses`: `azure-llmops-workshop`
- matching `courses.csv` `Course ID`: `azure-llmops-workshop`

### Goals field

`courses.csv` `Goals` should be semicolon-separated goal names.
If a goal does not exist yet, publisher mapping may create it (based on mapping decision settings).
