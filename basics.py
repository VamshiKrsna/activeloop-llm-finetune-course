import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

input_prompt = "Hello, how are you?"

response = client.chat.completions.create(
  model="llama3-8b-8192",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f'Translate the following English text to French: "{input_prompt}"'}
  ],
)

# print(type(response))
# print(response['choices'][0]['message']['content'])

print(f"Your Prompt : {input_prompt}")

print(response.choices[0].message.content)