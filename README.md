# Sunshine Backend Crop Assistant

Azure Functions backend for an AI-powered crop recommendation chatbot using Azure OpenAI.

## Features

- HTTP-triggered Azure Function for chat completions
- Integration with Azure OpenAI for intelligent crop suggestions
- Conversation history support
- Secure function-level authentication

## Prerequisites

- Python 3.13
- Azure Functions Core Tools
- Azure OpenAI service instance
- Azure Function App for deployment

## Environment Variables

Configure the following environment variables in your Azure Function App:

- `AOAI_KEY` - Azure OpenAI API key
- `AOAI_ENDPOINT` - Azure OpenAI endpoint URL
- `AOAI_DEPLOYMENT` - Azure OpenAI deployment name
- `AOAI_API_VERSION` - API version (default: 2024-12-01-preview)

## API Endpoint

### POST /api/HTTPTriggerAI2

Request body:
```json
{
  "conversation": [
    {"role": "user", "content": "What crops should I plant in spring?"}
  ]
}
```

Response:
```json
{
  "reply": "Based on spring conditions, I recommend..."
}
```

## Deployment

Automated deployment to Azure Functions via GitHub Actions on push to main branch.

## Project Structure

```
function_app/
├── function_app.py      # Main function handler
├── requirements.txt     # Python dependencies
└── .funcignore         # Files to exclude from deployment
```
