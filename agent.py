#from llm import parse_intent
from ollama import parse_intent
from executor import execute
from safety import validate
from rich import print

print("[bold green]K8s AI Agent CLI[/bold green]")
print("Type 'exit' to quit\n")

while True:
    user_input = input(">>> ")

    if user_input.lower() == "exit":
        break

    try:
        intent = parse_intent(user_input)
        validate(intent)
        result = execute(intent)

        print("[cyan]Intent:[/cyan]", intent)
        print("[green]Result:[/green]", result)

    except Exception as e:
        print("[red]Error:[/red]", str(e))