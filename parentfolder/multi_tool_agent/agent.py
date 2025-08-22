# Filename: agent.py
import sys
import os

# This is the crucial fix:
# It adds your project's root directory (AGENT/) to the list of places
# Python looks for modules, ensuring it can find the 'tools' package.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from google.adk.agents import Agent

# This import now correctly points to the 'functions.py' file inside the 'tools' package
from tools.functions import get_weather, get_current_time, create_notion_page

root_agent = Agent(
    name="multi_skill_agent",
    model="gemini-1.5-flash",
    description=(
        "Agent to answer questions about time, weather, and to save notes."
    ),
    instruction=(
        "You are a helpful agent. You can answer user questions about the time "
        "and weather in a city. You can also create pages in Notion to save notes."
    ),
    tools=[get_weather, get_current_time, create_notion_page],
)