import os
import json
import logging
import azure.functions as func
from openai import AzureOpenAI

# Create the Function App with secure function-level auth
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Load Azure OpenAI config from environment variables
AOAI_KEY = os.environ.get("AOAI_KEY")
AOAI_ENDPOINT = os.environ.get("AOAI_ENDPOINT")
AOAI_DEPLOYMENT = os.environ.get("AOAI_DEPLOYMENT")
AOAI_API_VERSION = os.environ.get("AOAI_API_VERSION", "2024-12-01-preview")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=AOAI_KEY,
    azure_endpoint=AOAI_ENDPOINT,
    api_version=AOAI_API_VERSION
)

@app.route(route="HTTPTriggerAI2", methods=["POST"])
def HTTPTriggerAI2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    try:
        # Get the prompt from JSON body
        req_body = req.get_json()
        prompt = req_body.get("conversation", "")

        if not prompt:
            return func.HttpResponse(
                json.dumps({"error": "No prompt provided"}),
                status_code=400,
                mimetype="application/json"
            )
        
        chatMessages = [{"role": "system", "content": "You are a helpful assistant."}]
        for p in prompt:
            chatMessages.append(p)

        # Call Azure OpenAI
        response = client.chat.completions.create(
            model=AOAI_DEPLOYMENT,
            messages=chatMessages
        )

        reply = response.choices[0].message.content

        # Return JSON to frontend
        return func.HttpResponse(
            json.dumps({"reply": reply}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error in HTTPTriggerAI2: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
