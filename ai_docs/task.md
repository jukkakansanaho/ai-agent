Please analyze and fix the Task: $ARGUMENTS.

Follow these steps:

# PLAN
1. Use Task/Sub-task description (in the Task List) to get the task details
2. Understand the problem described in the Task
3. Ask clarifying questions if necessary
4. Understand the prior art for this issue
- Search the `/specs` diretory for previous thoughts related to the issue.
- Search PRs to see if you can find history on this issue.
- Search the codebase for relevant files.
5. Think harder about how to break the Task down into a series of small, manageable tasks.
6. Document your plan in a new spec
- include the issue name in the filename
7. Document Task's Technical Specification in `/specs` directory using `/ai_docs/task-technical-specification-template.md` as an template

# CREATE
- Create a new branch for the Task.
- Solve the Task in small, manageable steps, according to your plan.
- Create unit test for the Task
- Commit you changes after each step.

# TEST
- Test changes in branch.
- If the tests are failing, fix them
- Ensure that all tests are passing before moving on to the next step.

# DEPLOY
- Open a PR, run the tests, and request a review.
 
Remember to use the GitHub CLI (`gh`) for all GitHhub-related tasks.