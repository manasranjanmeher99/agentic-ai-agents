# 🤖 CrewAI Agentic AI Projects

This folder contains **CrewAI-based Agentic AI projects** demonstrating how Large Language Models (LLMs) can be combined with AI agents, tasks, tools, and multi-agent workflows.

## 📁 Project Structure

```text
crewai/
│
├── .gitignore
├── README.md
├── crewai_with_gemini.ipynb
├── crewai_with_openai.ipynb
└── requirements.txt
```

## 🚀 Projects

### 🔹 CrewAI with Gemini

**File:** `crewai_with_gemini.ipynb`

A CrewAI notebook demonstrating a multi-agent workflow powered by **Google Gemini**.

The workflow uses specialized agents to collaborate on AI research and content generation.

### 🔹 CrewAI with OpenAI

**File:** `crewai_with_openai.ipynb`

A CrewAI notebook demonstrating an agent-based workflow using **OpenAI models**.

The project shows how agents can perform research and transform the gathered information into useful technical content.

## 🧠 What is CrewAI?

**CrewAI** is a framework for building collaborative AI agent systems.

Instead of using a single LLM to perform every step, a CrewAI application can divide a problem into specialized roles.

For example:

```text
                    User Request
                         │
                         ▼
                    ┌─────────┐
                    │  Crew   │
                    └────┬────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Research Agent          Writer Agent
              │                     │
              └──────────┬──────────┘
                         ▼
                    Final Output
```

## 🛠️ Technologies Used

- Python
- CrewAI
- Generative AI
- Large Language Models (LLMs)
- Google Gemini
- OpenAI
- Jupyter Notebook

## ⚙️ Installation

Create and activate a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

> **Note:** Your current file is named `requirements.txt.txt` in the screenshot.  
> Rename it to **`requirements.txt`** so the installation command above works normally.

Alternatively, if you keep the current filename:

```bash
pip install -r requirements.txt.txt
```

## 🔐 API Keys

The Gemini and OpenAI notebooks require their respective API keys.

Store API keys in a `.env` file rather than directly inside the notebook.

Example:

```env
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key
```

⚠️ **Never upload your `.env` file or API keys to GitHub.**

The `.gitignore` file is included to help prevent sensitive files from being committed.

## ▶️ Running the Notebooks

Start Jupyter Notebook:

```bash
jupyter notebook
```

Then open either:

```text
crewai_with_gemini.ipynb
```

or:

```text
crewai_with_openai.ipynb
```

Run the notebook cells in order.

## 📌 Learning Objectives

These projects demonstrate:

- AI agent creation
- Agent roles and goals
- Task definition
- Multi-agent collaboration
- Sequential agent workflows
- LLM integration
- AI-powered research
- AI content generation
- CrewAI fundamentals

## 🔮 Future Improvements

- Add more CrewAI agents
- Add web-search tools
- Add RAG-based agents
- Build a Streamlit interface
- Add persistent agent memory
- Create specialized Data Analyst agents
- Create Coding Agents
- Build larger multi-agent workflows
- Add more LLM providers

## 👨‍💻 Author

**Manas Ranjan Meher**

---

⭐ This project is part of my learning journey in **Generative AI and Agentic AI**.
