from django.shortcuts import render
from django.http import  HttpResponse, JsonResponse
from .models import Education,Image,WorkExperience, Projects,articles_certification_accomplishments
from django.views.decorators.csrf import csrf_exempt
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


# Fetching Education field data from database
education=Education.objects.all()
ed_Uclan=Education.objects.filter(UniversityName='University of Central Lancashire').first()
ed_lpu=Education.objects.filter(UniversityName='Lovely Professional University').first()
content_Uclan=ed_Uclan.content.split(';')
content_lpu=ed_lpu.content.split(';')
lpu_array=[ed_lpu,content_lpu]
uclan_array=[ed_Uclan,content_Uclan]

#Fetching work experience from database
dataanalyst_experience=WorkExperience.objects.filter(CompanyName='Data Analyst at Aveit Solutions Pvt Ltd').first()
freelance_experience=WorkExperience.objects.filter(CompanyName='Freelance Web Developer at KrishChem Fertilisers').first()
content_dataanalyst=dataanalyst_experience.JobResponsibilities.split(';')
content_freelance=freelance_experience.JobResponsibilities.split(';')
print(content_freelance)
dataanalyst_array=[dataanalyst_experience,content_dataanalyst]
freelance_array=[freelance_experience,content_freelance]

#Fetching Projects from database

#Leaf Disease Detection
leaf_disease_detection=Projects.objects.filter(ProjectName='Leaf Disease Detection').first()
leaf_disease_project_name= leaf_disease_detection.ProjectName
leaf_disease_project_description=leaf_disease_detection.ProjectDescription
leaf_disease_technologies_used=leaf_disease_detection.TechnologiesUsed
leaf_disease_images=leaf_disease_detection.ProjectImage
leaf_disease_array=[leaf_disease_images,leaf_disease_project_name,leaf_disease_project_description,leaf_disease_technologies_used]
print(f'leaf disease detection:{leaf_disease_array}')

# Covid Data Analysis
covid_data_analysis=Projects.objects.filter(ProjectName='Covid Data Analysis').first()
covid_data_analysis_project_name=covid_data_analysis.ProjectName
covid_data_analysis_project_description=covid_data_analysis.ProjectDescription
covid_data_analysis_technologies_used=covid_data_analysis.TechnologiesUsed
covid_data_image=covid_data_analysis.ProjectImage
covid_data_array=[covid_data_image,covid_data_analysis_project_name,covid_data_analysis_project_description,covid_data_analysis_technologies_used]
print(f'Covid Data Analysis:{covid_data_array}')

# Hospital Cypher
hospital_cypher=Projects.objects.filter(ProjectName='Hospital Cypher').first()
hospital_cypher_project_name=hospital_cypher.ProjectName
hospital_cypher_project_description=hospital_cypher.ProjectDescription
hospital_cypher_technologies_used=hospital_cypher.TechnologiesUsed
hospital_image=hospital_cypher.ProjectImage
hospital_cypher_array=[hospital_image,hospital_cypher_project_name,hospital_cypher_project_description,hospital_cypher_technologies_used]

# Hotel Cancellation Analysis
hotel_cancellation=Projects.objects.filter(ProjectName='Hotel Cancellation Analysis').first()
hotel_cancellation_project_name=hotel_cancellation.ProjectName
hotel_cancellation_project_description=hotel_cancellation.ProjectDescription
hotel_cancellation_technologies_used=hotel_cancellation.TechnologiesUsed
hotel_cancellation_image=hotel_cancellation.ProjectImage
hotel_cancellation_array=[hotel_cancellation_image,hotel_cancellation_project_name,hotel_cancellation_project_description,hotel_cancellation_technologies_used]

#Fetching articles and certifications from database
articles=articles_certification_accomplishments.objects.all()
articles_array=[articles[0],articles[1],articles[2]]

def home(request):
    """
    Renders the home page with context data including education, work experience, and projects.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page with the provided context.
    """
    context={
        'education':[uclan_array,lpu_array],
        'work_experience':[dataanalyst_array,freelance_array],
        'Projects':[leaf_disease_array,hospital_cypher_array,covid_data_array,hotel_cancellation_array],
        'articles':articles_array
    }
    return render(request,'website/home.html',context)


def run_flow(message: str) -> dict:
    """
    Sends a message to the Langflow API and returns the response.

    Args:
        message (str): The message to send to the API.

    Returns:
        dict: The response from the API.
    """
    # Construct the API URL
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    # Define the payload with the message and types
    payload = {
        "input_value": message,
        "output_type": 'chat',
        "input_type": 'chat',
    }

    # Set the headers including the authorization token
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}

    # Send the POST request to the API
    response = requests.post(api_url, json=payload, headers=headers)

    # Return the JSON response
    return response.json()

@csrf_exempt

def get_chatbot_response(request):

    """
Handles the chatbot response for a given user message.

This view function is exempt from CSRF verification. It expects a JSON payload
in the request body containing a 'message' key. The function processes the 
user's message and returns a JSON response with the processed message.

Args:
    request (HttpRequest): The HTTP request object containing the JSON payload.

Returns:
    JsonResponse: A JSON response containing the processed message.
"""
    data = json.loads(request.body)
    user_message = data['message']
    # Process message here
    response_message =run_flow(user_message)['outputs'][0]['outputs'][0]['results']['message']['text']
    return JsonResponse({'response': response_message})