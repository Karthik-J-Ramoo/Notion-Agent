# Filename: tools/functions.py

import os
import json
import requests
import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

# This line loads the variables from your .env file
load_dotenv()

# Debug: Print to verify environment variables are loaded (remove in production)
print(f"NOTION_API_KEY loaded: {'Yes' if os.environ.get('NOTION_API_KEY') else 'No'}")
print(f"NOTION_DATABASE_ID loaded: {'Yes' if os.environ.get('NOTION_DATABASE_ID') else 'No'}")

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city."""
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": "The weather in New York is sunny with a temperature of 25 degrees Celsius (77 degrees Fahrenheit).",
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone information for {city}.",
        }
    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}

def create_notion_page(title: str) -> dict:
    """
    Creates a new page with a specified title in a Notion database. 
    Use this to take notes or save information.
    """
    api_key = os.environ.get("NOTION_API_KEY")
    database_id = os.environ.get("NOTION_DATABASE_ID")

    if not api_key or not database_id:
        return {"status": "error", "error_message": "Notion API Key or Database ID is not configured."}

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }
    payload = {
        "parent": {"database_id": database_id},
        "properties": {
            "Title": {  # Try "Title" instead of "Name"
                "title": [{"text": {"content": title}}]
            }
        },
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return {"status": "success", "report": f"Successfully created the page '{title}' in Notion."}
        else:
            return {"status": "error", "error_message": f"Failed to create Notion page. Status: {response.status_code}, Error: {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "error_message": f"Failed to create Notion page. Network error: {str(e)}"}