# 🤖 AI Multi-Agent Project

A collection of AI agent projects built with **Python**, **Google Gemini**, **Groq**, and multi-agent frameworks. This repository contains experiments and applications for cricket analysis, financial/news analysis, and AI-powered assistants.

---

## 📌 Project Overview

This project demonstrates how multiple AI agents can be created for different tasks such as:

- 🏏 Cricket information and analysis
- 📰 Cricket/news research
- 📊 Financial and news analysis
- 🤖 Gemini-powered AI agents
- ⚡ Groq-powered AI agents
- 🌐 AI applications with a web interface

The project is organized into separate Python files so that each agent or application can be developed and tested independently.

---

## 📂 Project Structure

```text
agent/
│
├── .env.example
├── README.md
├── requirements.txt
│
├── app.py
│
├── cricket_agent_gemini.py
├── cricket_app_agent.py
│
├── groq_agent.py
├── groq_agent1.py
│
└── multiagent_financialnew_analysis.py
```

---

## 📄 File Description

### `app.py`

Main application entry point.

It can be used to provide a user interface for interacting with the AI agent system.

---

### `cricket_agent_gemini.py`

Gemini-powered cricket agent.

Typical responsibilities include:

- Searching cricket information
- Answering cricket-related questions
- Getting recent match information
- Providing player information
- Generating cricket analysis using Gemini

---

### `cricket_app_agent.py`

Cricket AI application layer.

This file can be used to connect the cricket agent with an application interface and allow users to submit cricket-related questions.

Example questions:

```text
What is the latest cricket score?

Tell me about Virat Kohli's recent performance.

What are the latest cricket news updates?

What are the upcoming India matches?
```

---

### `groq_agent.py`

AI agent implementation using a Groq-powered language model.

This file demonstrates how to create an AI assistant using Groq models.

---

### `groq_agent1.py`

An additional Groq agent implementation for experimenting with different prompts, models, tools, or agent configurations.

---

### `multiagent_financialnew_analysis.py`

Multi-agent system for financial and news analysis.

The application can be extended to use multiple specialized agents for tasks such as:

- Financial research
- Company analysis
- Market/news research
- News summarization
- Combining information from multiple agents

---

### `requirements.txt`

Contains the Python dependencies required to run the project.

Install them with:

```bash
pip install -r requirements.txt
```

---

### `.env.example`

Template for environment variables and API keys.

Create a `.env` file based on this file:

```bash
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

**Never commit your real `.env` file or API keys to GitHub.**

---

# 🧠 Architecture

The overall concept of the project is:

```text
                         User
                           │
                           ▼
                    Application / UI
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        Gemini Agent    Groq Agent   Multi-Agent System
             │             │             │
             ▼             ▼             ▼
          Research       Analysis      Specialized
          & Answers      & Answers       Agents
             │             │             │
             └─────────────┴─────────────┘
                           │
                           ▼
                      Final Response
```

---

# 🏏 Cricket Agent

The cricket-related files demonstrate how an AI agent can be used to answer cricket questions and retrieve current information.

Example workflow:

```text
User Question
     │
     ▼
Cricket AI Agent
     │
     ▼
Search / Knowledge Retrieval
     │
     ▼
Gemini Model
     │
     ▼
Cricket Analysis
     │
     ▼
User
```

Example:

```text
User:
"Give me the latest India vs Australia score and
Virat Kohli's recent statistics."

Agent:
1. Searches for relevant information
2. Identifies the required cricket data
3. Processes the information
4. Generates a structured response
```

---

# 💰 Financial & News Multi-Agent System

The financial/news project demonstrates the concept of specialized AI agents.

```text
                 User Query
                     │
                     ▼
              Main AI Agent
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Financial    News       Research
        Agent      Agent        Agent
          │          │          │
          └──────────┼──────────┘
                     ▼
              Combined Analysis
                     │
                     ▼
                Final Answer
```

This architecture can be extended with additional agents such as:

- Stock Analysis Agent
- Market News Agent
- Company Research Agent
- Financial Report Agent
- Risk Analysis Agent

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini | Generative AI / LLM |
| Groq | Fast LLM inference |
| AI Agents | Task automation and reasoning |
| Multi-Agent Architecture | Specialized task delegation |
| Gradio / Web UI | Application interface |
| DuckDuckGo Search | Web information retrieval |
| python-dotenv | Environment variable management |

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/manasranjanmeher99/agentic-ai-agents
cd agent
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure API Keys

Copy `.env.example` to `.env`.

Windows:

```bash
copy .env.example .env
```

Linux/macOS:

```bash
cp .env.example .env
```

Then add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

# ▶️ Running the Project

Depending on the application you want to test:

### Main application

```bash
python app.py
```

### Gemini Cricket Agent

```bash
python cricket_agent_gemini.py
```

### Cricket Application Agent

```bash
python cricket_app_agent.py
```

### Groq Agent

```bash
python groq_agent.py
```

### Groq Agent 1

```bash
python groq_agent1.py
```

### Financial & News Multi-Agent

```bash
python multiagent_financialnew_analysis.py
```

---

# 🔐 Environment Variables

Store API keys in `.env` instead of directly inside Python files.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Add `.env` to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# 🚀 Future Improvements

- [ ] Add more specialized cricket agents
- [ ] Add a dedicated live cricket API
- [ ] Add player statistics API integration
- [ ] Add persistent conversation memory
- [ ] Add agent tool calling
- [ ] Add RAG-based knowledge retrieval
- [ ] Add Streamlit/Gradio dashboard
- [ ] Add logging and error handling
- [ ] Add unit tests
- [ ] Deploy the application online
- [ ] Add GitHub Actions CI/CD

---

# 🎯 Learning Objectives

This project is useful for learning:

- Generative AI
- LLM integration
- AI agents
- Multi-agent systems
- Prompt engineering
- Tool calling
- Web search integration
- API integration
- Python application development
- AI application deployment

---

# 👨‍💻 Author

**Manas Meher**

MCA Graduate | Aspiring Software Engineer | Data Science & Generative AI Learner

Interested in:

- Python
- Data Science
- Machine Learning
- Generative AI
- Agentic AI
- Web Development
- SQL

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
