# just a simple code example of grok-ai api usage

import os

# pip install openai
from openai import OpenAI

# Set your API key here
grokapi = "xai-XXXXXXXXXXXXXXXXXX" 

# Make a call to function using openai library
client = OpenAI(api_key=grokapi, base_url="https://api.x.ai/v1")

completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "system", "content": "You are grok, an openai"},
        {"role": "user", "content": "How does X algorithm work?"}
    ]
)

print(completion.choices[0].message)