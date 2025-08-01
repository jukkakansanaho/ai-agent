---
description: 
globs: 
alwaysApply: false
---
# Rule: Generating a Task List from a PRD

## Goal

To guide an AI assistant in creating a detailed, step-by-step task list in Markdown format based on an existing Product Requirements Document (PRD). The task list should guide a developer through implementation.

## Output

- **Format:** Markdown (`.md`)
- **Location:** `/specs/`
- **Filename:** `tasks-[prd-file-name].md` (e.g., `tasks-prd-user-profile-editing.md`)

## Process

1.  **Receive PRD Reference:** The user points the AI to a specific PRD file
2.  **Analyze PRD:** The AI reads and analyzes the functional requirements, user stories, and other sections of the specified PRD.
3.  **Phase 1: Generate Parent Tasks:** Based on the PRD analysis, create the file and generate the main, high-level tasks required to implement the feature. Use your judgement on how many high-level tasks to use. It's likely to be about 5. Present these tasks to the user in the specified format (without sub-tasks yet). Inform the user: "I have generated the high-level tasks based on the PRD. Ready to generate the sub-tasks? Respond with 'Go' to proceed."
4.  **Wait for Confirmation:** Pause and wait for the user to respond with "Go".
5.  **Phase 2: Generate Sub-Tasks:** Once the user confirms, break down each parent task into smaller, actionable sub-tasks necessary to complete the parent task. Ensure sub-tasks logically follow from the parent task and cover the implementation details implied by the PRD.
6.  **Identify Relevant Files:** Based on the tasks and PRD, identify potential files that will need to be created or modified. List these under the `Relevant Files` section, including corresponding test files if applicable.
7.  **Generate Final Output:** Combine the parent tasks, sub-tasks, relevant files, and notes into the final Markdown structure.
8.  **Save Task List:** Save the generated document in the `/specs/` directory with the filename `tasks-[prd-file-name].md`, where `[prd-file-name]` matches the base name of the input PRD file (e.g., if the input was `prd-user-profile-editing.md`, the output is `tasks-prd-user-profile-editing.md`).

## Output Format

The generated task list _must_ follow this structure:

```markdown
## Relevant Files

- `path/to/potential/file1.py` - Brief description of why this file is relevant (e.g., Contains the main component for this feature).
- `/test/test_file1.py` - Unit tests for `file1.py`.
- `path/to/another/file.py` - Brief description (e.g., API route handler for data submission).
- `/test/test_file.py` - Unit tests for `another/file.py`.
- `path/to/test_e2e/test_file.py` - Integration and end-to-end tests for `another/file.py`.
- `lib/utils/helpers.py` - Brief description (e.g., Utility functions needed for calculations).
- `lib/utils/helpers.test.py` - Unit tests for `helpers.py`.

### Notes

- Unit tests should typically be placed in `/test` directory parallel with the code files they are testing (e.g., `my_component.py` inside `/` and `test_my_component.py` inside parallel `/test` directory).
- Integration and end-to-end should typically be placed in `/test_e2e` directory parallel with `/test` directory.
- Use `python3 -m unittest discover -v -s . [optional/path/to/test/file]` to run python unit tests. Running without a path executes all tests found by the python unittest configuration.
- Use `pytest test_e2e` to run python integration and end-to-end tests.
- Use `gh` command and `github_actions_runner.txt` inside `/ai_docs` directory to test the GitHub Actions.

## Tasks

- [ ] 1.0 Parent Task Title
  - [ ] 1.1 [Sub-task description 1.1]
  - [ ] 1.2 [Sub-task description 1.2]
- [ ] 2.0 Parent Task Title
  - [ ] 2.1 [Sub-task description 2.1]
- [ ] 3.0 Parent Task Title (may not require sub-tasks if purely structural or configuration)
```

## Interaction Model

The process explicitly requires a pause after generating parent tasks to get user confirmation ("Go") before proceeding to generate the detailed sub-tasks. This ensures the high-level plan aligns with user expectations before diving into details.

## Target Audience

Assume the primary reader of the task list is a **junior developer** who will implement the feature.
