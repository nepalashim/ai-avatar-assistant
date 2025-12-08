AI Avatar Assistant

A conversational AI system designed to manage customer interactions for hotels and service-based businesses. This project brings together multiple modern technologies to deliver smooth voice-driven communication, automated workflows, and a realistic AI avatar experience.

Features

Voice-Based Interaction
Utilizes LiveKit with an AI speech model to provide natural, real-time conversations.

Avatar Interface
Integrates with Tavus to display a lifelike AI avatar during interactions.

Automated Workflows
Uses an n8n MCP (Model Context Protocol) server to run complex hotel or business logic.

AI Agent Architecture
Custom-built agent that handles queries, bookings, service requests, and operational tasks.

Knowledge Integration
Includes a knowledge management system for storing hotel data, FAQs, and service information.

Technologies Used

LiveKit – Real-time communication platform for audio and video

AI Speech/Language Model – Used for conversational understanding

Tavus – Avatar rendering and interaction technology

n8n MCP Server – Automation and integration service

Python – Main development language for the agent system

Prerequisites

Python 3.8+

LiveKit account and credentials

API key for your chosen AI model

Tavus account with necessary keys

Running instance of an n8n MCP server

Installation

Clone the repository:

git clone https://github.com/nepalashim/ai-avatar-assistant.git
cd ai-avatar-assistant


Install dependencies:

pip install -r requirements.txt


Set environment variables:

Duplicate .env.example as .env

Insert all required API keys and configuration values

Run the agent:

python3 agent.py dev


After starting the server, open the LiveKit Playground and connect to your agent.

Configuration

Environment variables control all external services and integrations.
Refer to .env.example for required fields, including:

LiveKit: URL, API key, and API secret

AI Model Provider: API keys

Tavus: Persona ID, replica ID, and API key

n8n: MCP server endpoint

Project Structure
ai-avatar-assistant/
├── agent.py           # Main agent implementation
├── server.py          # Application entry point
├── tools.py           # Tool definitions and utilities
├── prompts.py         # Prompt templates for AI behavior
├── mcp_client/        # MCP client utilities
│   ├── agent_tools.py
│   ├── server.py
│   └── util.py
├── KMS/               # Knowledge system and logs
│   └── logs/
├── test/              # Test files
└── requirements.txt   # Dependency list

Use Cases

Handling guest check-in and check-out

Managing reservations

Providing hotel information and amenity details

Supporting room service requests

Acting as a digital concierge

Automating routine customer service tasks

Security

Sensitive configuration values are stored in a .env file and excluded from version control

API keys must be protected and updated periodically

Production deployments should follow standard security and infrastructure best practices
