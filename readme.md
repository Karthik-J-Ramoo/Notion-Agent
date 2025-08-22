# Multi-Tool Agent with Notion Integration

A Python-based AI agent that can provide weather information, current time, and create pages in Notion databases using Google's Agent Development Kit (ADK).

## Features

- 🌤️ **Weather Reports**: Get current weather information for supported cities
- 🕐 **Time Queries**: Get current time in different timezones
- 📝 **Notion Integration**: Create new pages in your Notion database
- 🤖 **AI-Powered**: Uses Google's Gemini 1.5 Flash model for natural language processing

## Project Structure

```
Agent/
├── parentfolder/
│   └── multi_tool_agent/
│       ├── agent.py                 # Main agent configuration
│       ├── .env                     # Environment variables (not tracked)
│       └── tools/
│           ├── __init__.py          # Package initialization
│           └── functions.py         # Tool functions implementation
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

## Prerequisites

- Python 3.8+
- Google Cloud Project with Generative AI API enabled
- Notion account with API access
- Virtual environment (recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Karthik-J-Ramoo/Notion-Agent.git
cd Notion-Agent
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install google-adk requests python-dotenv
```

### 4. Set Up Google ADK

1. **Create a Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one

2. **Enable the Generative AI API**:
   - Navigate to APIs & Services → Library
   - Search for "Generative Language API"
   - Click "Enable"

3. **Create API Credentials**:
   - Go to APIs & Services → Credentials
   - Click "Create Credentials" → API Key
   - Copy the generated API key

### 5. Set Up Notion Integration

1. **Create a Notion Integration**:
   - Go to [Notion Integrations](https://www.notion.so/my-integrations)
   - Click "New integration"
   - Give it a name and select capabilities
   - Copy the generated secret token

2. **Create a Notion Database**:
   - Create a new page in Notion
   - Add a database with at least a "Title" property
   - Share the database with your integration

3. **Get Database ID**:
   - Copy the database URL: `https://notion.so/workspace/DATABASE_ID?v=...`
   - Extract the DATABASE_ID (32-character string)

### 6. Configure Environment Variables

Create a `.env` file in `parentfolder/multi_tool_agent/`:

```properties
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your_google_api_key_here
NOTION_API_KEY=your_notion_secret_token_here
NOTION_DATABASE_ID=your_notion_database_id_here
```

**Important**: Never commit the `.env` file to version control. It's already included in `.gitignore`.

## How It Works

### Agent Architecture

The agent is built using Google's Agent Development Kit (ADK) with the following components:

1. **Agent Configuration** (`agent.py`):
   - Uses Gemini 1.5 Flash model for language understanding
   - Configured with specific tools and instructions
   - Handles natural language queries and tool selection

2. **Tool Functions** (`tools/functions.py`):
   - `get_weather()`: Returns weather information for supported cities
   - `get_current_time()`: Returns current time in specified timezones
   - `create_notion_page()`: Creates new pages in Notion database

### Notion Integration Logic

The Notion integration works through the following process:

1. **Authentication**: Uses the Notion API key to authenticate requests
2. **Database Connection**: Connects to the specified database using the database ID
3. **Page Creation**: Creates new pages with the following structure:
   ```json
   {
     "parent": {"database_id": "your_database_id"},
     "properties": {
       "Title": {
         "title": [{"text": {"content": "Your Page Title"}}]
       }
     }
   }
   ```
4. **Property Mapping**: The agent maps the user's input to the "Title" property of the database
5. **API Request**: Sends a POST request to `https://api.notion.com/v1/pages` with proper headers

### Supported Cities

**Weather & Time**:
- New York (more cities can be added by extending the functions)

## Usage

### Running the Agent

```bash
cd parentfolder/multi_tool_agent
python agent.py
```

### Example Queries

- "Create a note titled 'Meeting Notes'"
- "Add a page called 'Project Ideas' to my Notion"

### Common Issues

1. **"Name is not a property that exists"**:
   - Check your Notion database properties
   - Ensure the title column is named "Title"
   - Update the property name in `create_notion_page()` if different

2. **API Keys not loading**:
   - Verify `.env` file location
   - Check environment variable names
   - Ensure `load_dotenv()` is called

3. **Import errors**:
   - Verify virtual environment is activated
   - Install missing dependencies
   - Check Python path and package structure

### Debug Mode

The application includes debug prints to verify environment variables are loaded. You'll see:
```
NOTION_API_KEY loaded: Yes/No
NOTION_DATABASE_ID loaded: Yes/No
```

## Security

- **API Keys**: Never commit API keys to version control
- **Environment Variables**: Use `.env` file for sensitive data
- **Regeneration**: Regenerate API keys if accidentally exposed

## Links

- [Google ADK Documentation](https://developers.google.com/adk)
- [Notion API Documentation](https://developers.notion.com/)
