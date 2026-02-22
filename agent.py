from ollama import parse_intent
from safety import validate
from executor import execute
from rich import print

def handle_message(user_input, auto_confirm=False):
    intent = parse_intent(user_input)
    validate(intent)

    if intent["action"] == "scale_deployment" and not auto_confirm:
        return {
            "intent": intent,
            "message": "CONFIRM_REQUIRED"
        }

    result = execute(intent)

    return {
        "intent": intent,
        "result": result
    }
