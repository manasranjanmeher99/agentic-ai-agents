# 🤖 CrewAI Projects

A collection of **CrewAI-based Agentic AI and Multi-Agent projects** built with Python and Large Language Models (LLMs).

## 📁 Folder Structure

```text
crewai/
│
├── README.md
│
├── gemini_research_crew/
│   ├── agents.py
│   ├── tasks.py
│   ├── crew.py
│   ├── main.py
│   ├── requirements.txt
│   ├── .env.example
│   └── original_notebook.ipynb
│
└── openai_research_crew/
    ├── agents.py
    ├── tasks.py
    ├── crew.py
    ├── main.py
    ├── requirements.txt
    ├── .env.example
    └── original_notebook.ipynb
```

## 🚀 Projects

### 1. Gemini Research Crew

A multi-agent research workflow using CrewAI and Google Gemini.

**Agents:**
- 🔎 **AI Researcher** — researches Generative AI and Agentic AI trends.
- ✍️ **Technical Writer** — converts research into structured technical content.
- 🧐 **AI Reviewer** — reviews and polishes the final content.

**Workflow:**

```text
AI Researcher
      ↓
Technical Writer
      ↓
AI Reviewer
      ↓
Final Workshop-Ready Content
```

Research areas include:
- Large Language Models (LLMs)
- Agentic AI
- Multi-Agent Systems
- Enterprise AI adoption
- AI tools and frameworks

### 2. OpenAI Research Crew

A two-agent research and content-generation workflow.

**Agents:**
- 🔎 **Senior Research Analyst** — researches recent AI developments.
- ✍️ **Tech Content Strategist** — creates an engaging technical article.

**Workflow:**

```text
Senior Research Analyst
          ↓
Tech Content Strategist
          ↓
Final AI Article
```

The research agent uses a web-search tool to gather information before passing the research to the content strategist.

## 🧠 Concepts Demonstrated

- AI Agents
- Multi-Agent Systems
- Agent collaboration
- Task delegation
- Sequential workflows
- Tool usage
- Web research
- LLM integration
- Research automation
- Content generation
- AI-powered review workflows

## 🛠️ Technologies

- Python
- CrewAI
- Google Gemini
- OpenAI
- CrewAI Tools
- Serper Search
- python-dotenv
- Large Language Models (LLMs)
- Agentic AI

## ⚙️ Installation

Navigate to the project you want to run:

```bash
cd gemini_research_crew
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file using the appropriate `.env.example`.

### Gemini Project

```env
GOOGLE_API_KEY=your_google_api_key
```

### OpenAI Project

```env
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

⚠️ **Never commit API keys or `.env` files to GitHub.**

## ▶️ Running the Projects

### Gemini Research Crew

```bash
cd gemini_research_crew
python main.py
```

### OpenAI Research Crew

```bash
cd openai_research_crew
python main.py
```

## 📊 Agentic AI Workflow

```text
User Request
     │
     ▼
    Crew
     │
     ▼
Research Agent
     │
     ▼
Specialist / Writer Agent
     │
     ▼
Reviewer Agent
     │
     ▼
Final Output
```

## 🎯 Future Improvements

- [ ] More CrewAI projects
- [ ] RAG-based CrewAI systems
- [ ] Data Analysis Crew
- [ ] Coding Agent Crew
- [ ] Cricket Research Crew
- [ ] AI News Research Crew
- [ ] Streamlit interfaces
- [ ] Persistent agent memory
- [ ] More multi-agent workflows

## 📚 Learning Goals

This repository is part of my **Generative AI and Agentic AI learning journey**.

The main focus is:

**LLMs → Tools → Agents → Tasks → Crews → Multi-Agent Systems**

## 👨‍💻 Author

**Manas Meher**

MCA Graduate | Data Science | Generative AI | Agentic AI

---

⭐ If you find this repository useful, consider giving it a star!
