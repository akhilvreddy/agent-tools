[WORK IN PROGRESS]

A simple plug-and-play toolkit of real-world actions for AI agents - I was using these on local but wanted to throw it on GitHub for further growth. 

You can drop these tools into your agentic framework and get features like search, email, and Discord messaging.

Designed for **easy integration with LangChain, LangGraph, AutoGen, CrewAI, and custom agent frameworks**.

*No machine learning here, just simple APIs built for AI agents*

In this repository I've included `.env`-based auth, tests for endpoints, and plug-and-play integration.

---

## Included Tools

| Tool          | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `/search`     | Web search using DuckDuckGo or SerpAPI for real-world context + info        |
| `/email`      | Send + receive emails via SMTP (status reports, async agent comms)          |
| `/discord`    | Send Discord messages to a webhook for status alerts or logging             |
| `/refine`     | Agent self-evaluation + summary improvement loop using LLM (CoT cleanup)    |
| `/summarize`  | Summarize any input text or multi-doc context via OpenAI or local LLM       |
| `/toolshelf`  | Tool registry / catalog the agent can query for available actions           |
| `/plan`       | Generate action plans for a task using an LLM-powered planner                |
| `/reask`      | Let agents ask clarifying questions when uncertain (meta-cognition)         |
| `/critique`   | Critically analyze agent output and suggest revisions (safety layer)        |
| `/extract`    | Extract structured data from messy input (e.g., JSON from blob)             |
| `/memory`     | Simple file-based scratchpad / JSON memory for tool state                   |
| `/file-utils` | Tools for managing file actions (move, delete, read) for cleanup agents     |
| `/log`        | Agent event logger to local file or external endpoint                       |
| `/timestamp`  | Adds human-readable or UNIX timestamps to actions for temporal awareness    |

Tools that are a little more difficult (more prompt-engineering heavy, still working on these)

| Tool                  | Description                                                              |
|------------------------|--------------------------------------------------------------------------|
| `/beliefs`             | Track what the agent "believes" to be true right now                     |
| `/motivation`          | Specify why the agent is doing what it's doing (goal-aware action loop)  |
| `/hallucination-check` | Flag potential hallucinated info in LLM output                           |
| `/retry`               | Automatic retry wrapper with backoff for flaky tool calls                |
| `/metrics`             | Run evals or metrics like BLEU / accuracy / F1 on text output            |
| `/self-debug`          | Let the agent analyze its last failure and suggest fixes                 |
| `/report`              | Package run results + insights into markdown/pdf summary                 |

---

## Installation

1) Clone the repository either:
- The root of your `/Projects` folder (for reusability)
- Inside the repository of your agentic framework (for single project use)

```bash
git clone https://github.com/yourname/agent-tools.git
```

2) Install requirements
```bash
cd agent-tools
pip install -r requirements.txt
```
3) Create `.env` file and populate credentials
```bash
cp .env.example .env
```

You're now ready to use. 

---

## Usage

1) Web Search 
```python
from tools.search.search_tool import search_web

results = search_web("What are LLM agents?")
print(results)
```

This returns a string summary or top search results using SerpAPI (you can go into `/tools` and edit).

2) Send Email
```python
from tools.email.email_tool import send_email

send_email(
    to="recipient@example.com",
    subject="Agent Update",
    body="The task has been completed successfully."
)
```
Make sure your email and password are saved securely in .env

The rest of these tools follow pretty much the same format.

---

## Deploying (if not using LangChain / CrewAI / AutoGen)

Convert your `.env` to github secrets in Actions CI/CD. 

1) Make sure you have GitHub CLI: 
```bash
gh --version
```

2) Login to GitHub via CLI:
```bash
gh auth login
```

3) From root of your repo, run the following to push kv pairs to GitHub secrets:
```bash
while IFS='=' read -r key value
do
  if [[ $key != \#* && $key != "" ]]; then
    echo "Setting secret: $key"
    gh secret set "$key" --body "$value"
  fi
done < .env
```

---

These tools are built to drop into any agentic framework. You can:
- Wrap them in LangChain Tool objects
- Use them as function_calling targets in OpenAI agents
- Call them as-is in CrewAI or AutoGen action nodes