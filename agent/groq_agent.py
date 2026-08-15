
"""from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY=""

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True
)

agent.print_response("about nvidia stock")"""

import os
from phi.agent import Agent
from phi.model.groq import Groq

# Groq API Key
os.environ["GROQ_API_KEY"] = ""

# Create Agent
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True
)

# Ask the agent
agent.print_response("about Nvidia stock")