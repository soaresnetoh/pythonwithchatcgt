import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI.API_KEY')


messages = [ {"role":"system","content":
    "Translate the following English text to Protuguese:"} ]

while True:
    query = input("Solicitação: ")
    if messages:
        messages.append(
            {"role": "user","content": query},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role":"assistant","content":reply})