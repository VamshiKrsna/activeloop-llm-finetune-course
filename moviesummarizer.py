from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq

prompt = """
    summarize a movie story using emojis : 
    
    {movie}: 
"""

examples = [
    { "input":"Titanic","output":"🛳️🌊❤️🧊🎶🔥🚢💔👫💑"},
    { "input": "The Matrix", "output": "🕶️💊💥👾🔮🌃👨🏻‍💻🔁🔓💪" }
]


movie = "Requiem for a dream" # 🏠💊📦😵💸👀💔😔😩

client = Groq()

response = client.chat.completions.create(
  model="llama3-8b-8192",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt.format(movie = examples[0]["input"])},
    {"role":"assistant","content":prompt.format(movie=examples[1]["input"])},
    {"role": "user", "content": prompt.format(movie=examples[1]["input"])},
    {"role": "assistant", "content": examples[1]["output"]},
    {"role": "user", "content": prompt.format(movie=movie)},
  ]
)

# print(type(response))
# print(response['choices'][0]['message']['content'])

print(f"Your Prompt : {movie}")

print(response.choices[0].message.content)