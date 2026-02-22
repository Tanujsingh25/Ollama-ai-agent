#This file converts chat → JSON intent
from openai import OpenAI
from dotenv import load_dotenv
import json,os

load_dotenv()

print("API Key Loaded:", os.getenv("OPENAI_API_KEY") is not None)

client = OpenAI()

SYSTEM_PROMPT = """
You are a Kubernetes AI assistant.

Your job is to convert user commands into JSON.

Allowed actions:
- get_pods
- scale_deployment
- get_logs
- describe_resource

NEVER invent fields.
Return ONLY valid JSON.
"""

def parse_intent(user_input):
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
