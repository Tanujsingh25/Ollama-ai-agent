#This prevents dangerous commands
ALLOWED_ACTIONS = {
    "get_pods",
    "scale_deployment",
    "get_logs",
    "describe_resource"
}

def validate(intent):
    if intent["action"] not in ALLOWED_ACTIONS:
        raise Exception("Action not allowed")

    if intent["action"] == "scale_deployment":
        if intent["replicas"] > 10:
            raise Exception("Replica limit exceeded")

    return True