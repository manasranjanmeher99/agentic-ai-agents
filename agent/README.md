# 🏏 Cricket Analysis Agent

A multi-agent cricket assistant built with **Agno**, **Google Gemini**, and **DuckDuckGo**.

## Features

- 🏏 Live/recent cricket match score search
- 📊 Recent player statistics
- 📰 Latest cricket news
- 🤖 Multi-agent delegation
- 🔎 Web search through DuckDuckGo
- 📋 Markdown-formatted responses
- 🌐 Optional Gradio web interface

## Project Structure

```text
agent/
│
├── groq_agent.py
├── groq_agent1.py
├── multiagent_financialnew_analysis.py
│
├── cricket_match_agent.py
├── player_stats_agent.py
├── cricket_news_agent.py
├── cricket_team.py
├── app.py
│
├── requirements.txt
├── .env.example
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## Run from Terminal

```bash
python cricket_team.py
```

## Run the Gradio App

```bash
python app.py
```

Then open the local Gradio URL shown in the terminal.

## Example Questions

```text
What is the latest India vs Australia score?

Give me Virat Kohli's statistics from his last 5 matches.

What are the latest cricket news headlines?

What are the upcoming India cricket matches?

Summarize the current cricket situation.
```

## Architecture

```text
                    Cricket User
                         |
                         v
                Cricket Analysis Team
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
    Match Agent     Player Agent    News Agent
          |              |              |
          +--------------+--------------+
                         |
                         v
                  DuckDuckGo Search
                         |
                         v
                    Gemini Model
                         |
                         v
                  Final Response
```

## Important Note

DuckDuckGo is a general web-search tool. For guaranteed real-time cricket scores, a dedicated cricket/live-score API is preferable.

Never commit your `.env` file or expose your Gemini API key.
