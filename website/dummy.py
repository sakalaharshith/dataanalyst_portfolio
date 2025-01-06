# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import json
import os
import requests
from dotenv import load_dotenv
# Loading environment variables to access the application token
load_dotenv()

# Defining the base API URL, Langflow ID, Flow ID, Application Token, and Endpoint
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "a100d15b-27a4-4fd5-b036-65c85469ae71"
FLOW_ID = "83130adc-b8a5-4633-bbe6-591805d8a780"
APPLICATION_TOKEN =os.environ.get('APP_TOKEN') # Your application token
ENDPOINT = "sakbot" # The endpoint name of the flow


def run_flow(message: str) -> dict:
   
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type":'chat',
        "input_type": 'chat',
    }
    
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

results=run_flow('tell me about harshith')['outputs'][0]['outputs'][0]['results']['message']['text']
print(results)
