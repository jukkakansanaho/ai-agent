# AI Agent
AI Agent is a guided Boot.dev project. 
If you've ever used [Cursor](https://www.cursor.com/en) or [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) as an "[agentic](https://en.wikipedia.org/wiki/Agentic_AI)" AI editor, you'll understand what we're building in this project.

We're building a toy version of Claude Code using Google's [free Gemini API](https://ai.google.dev/gemini-api/docs)!
## Tools
* [Google AI Studio](https://aistudio.google.com/)

## Packages used
* [google-genai](https://pypi.org/project/google-genai/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

# How to use
* Install python
* run ```uv run ./main.py```

## Install and use Python uv
* install uv: ```curl -LsSf https://astral.sh/uv/install.sh | sh```
* initialize uv in the project: ```uv init```
    * creates .venv dir
* initialize venv: ```source .venv/bin/activate```
* add dependencies: ```uv add -r requirements.txt```
    * installs deps and creates ```uv.lock```

## Test Python code
* ```./test.sh```

## Install Coverage for code coverage
* ```python3 -m pip install coverage```
* ```./test_coverage.sh```

