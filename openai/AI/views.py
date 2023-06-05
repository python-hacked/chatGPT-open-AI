from django.shortcuts import render
import openai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_KEY', None)


def chatboot(request):
    chatbot_response = None
    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=messages,
            max_tokens=256,
            temperature=0.5
        )

        chatbot_response = response.choices[0].text.strip()

    return render(request, 'response.html', {'response': chatbot_response})
