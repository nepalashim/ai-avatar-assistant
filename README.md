# AI Avatar Assistant

A conversational AI system designed to manage customer interactions for hotels and service-based businesses. It integrates real-time voice communication, workflow automation, and a visual AI avatar to deliver an interactive guest experience.

## Features

### Real-Time Voice Interaction
Enables natural, continuous audio conversations using LiveKit.

### Avatar Interface
Integrates Tavus to display a realistic AI avatar during interactions.

### Workflow Automation
Uses an n8n MCP (Model Context Protocol) server to manage business logic, automate tasks, and integrate external systems.

### AI Agent System
Custom agent architecture capable of handling bookings, answering queries, processing service requests, and managing hotel operations.

### Knowledge Management
Includes a centralized knowledge module for hotel information, FAQs, and service data.

## Technologies Used
- **LiveKit** – Real-time audio/video communication  
- **AI Speech/Language Model** – Conversational AI processing  
- **Tavus** – Avatar rendering and interaction  
- **n8n MCP Server** – Workflow automation and integration  
- **Python** – Core programming language  

## Prerequisites
- Python 3.8 or higher  
- LiveKit credentials  
- AI model API key  
- Tavus API account  
- n8n MCP server instance  

## Installation

### Clone the Repository
git clone https://github.com/nepalashim/ai-avatar-assistant.git
cd ai-avatar-assistant
## Install Dependencies

pip install -r requirements.txt

Configure Environment Variables

Copy .env.example → .env

Fill in API keys and required credentials

### Start the Agent
python3 agent.py dev


After starting, open the LiveKit Playground and connect to your agent.

### Configuration

All settings are managed through environment variables. See .env.example for:

LiveKit: URL, API key, secret

AI Model: API key

Tavus: Persona ID, Replica ID, API key

n8n MCP: Server endpoint

### Project Structure
ai-avatar-assistant/
├── agent.py            # Core agent logic
├── server.py           # Main server entry point
├── tools.py            # Utilities and tool definitions
├── prompts.py          # AI prompt templates
├── mcp_client/         # MCP client implementation
│   ├── agent_tools.py
│   ├── server.py
│   └── util.py
├── KMS/                # Knowledge Management System
│   └── logs/
├── test/               # Test files
└── requirements.txt    # Python dependencies

### Use Cases

Guest check-in and check-out

Room booking and reservation management

Room service requests

Hotel information and amenity details

Digital concierge services

Automated customer support

### Security

All sensitive credentials are stored in .env (ignored by Git)

Keep API keys secure and rotate them regularly
