import json
import os
import requests
from django.http import JsonResponse
# from django.shortcuts import render
# from django.views import View
from dotenv import load_dotenv
from rest_framework.decorators import api_view

OPENAI_CHAT_COMPLETION_URL = 'https://api.openai.com/v1/chat/completions'

# Create your views here.
@api_view(['POST'])
def chatapi(request):
    if request.method == 'POST':
        userMessage = request.data.get('message')
        userId = request.data.get('userId')
        print("userdetals",userId)
        if not userMessage:
            return JsonResponse({"error": "Please provide a user input as a message parameter."}, status=400)
        load_dotenv()
        openai_api_key = os.environ.get('OPENAI_API_KEY')
        reqBody = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": userMessage}]   
        }
        headers = {
        'Authorization': f'Bearer {openai_api_key}',
        'Content-Type': 'application/json'
        }
        response = requests.post(OPENAI_CHAT_COMPLETION_URL, headers=headers, data=json.dumps(reqBody))
        if response.status_code == 200:
            # Extract the response from the API JSON response
            api_response = response.json()
            print('--> Response: ', api_response)
            chat_response = api_response['choices'][0]['message']['content']
            # we should store the message, reply in database
            return JsonResponse({'reply': chat_response}, status=200)
        print('--> Status: ',response.status_code)
        print('--> Error Response: ',response.json())
        return JsonResponse(response.json(), status=response.status_code)
    else:
        return JsonResponse({"error":"method not supported"}, status=405)