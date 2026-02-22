import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

SYSTEM_PROMPT = """
You are a Kubernetes AI assistant.

Convert the user's request into VALID JSON.

Allowed actions:
- get_pods
- scale_deployment
- get_logs

JSON formats:

get_pods:
{
  "action": "get_pods",
  "namespace": "default"
}

scale_deployment:
{
  "action": "scale_deployment",
  "name": "nginx",
  "namespace": "default",
  "replicas": 3
}

get_logs:
{
  "action": "get_logs",
  "pod": "pod-name",
  "namespace": "default"
}

Rules:
- Return ONLY JSON
- No explanation
- No markdown
"""

def parse_intent(user_input):
    prompt = f"""
{SYSTEM_PROMPT}

User input:
{user_input}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    raw_output = response.json()["response"].strip()
    return json.loads(raw_output)