import json

def ask_llm(prompt, system=None):
    fake_response = """
    {
        "name": "John Doe",
        "email": "john@example.com"
    }
    """
    return json.loads(fake_response)

result = ask_llm("Extract the name and email")

print(type(result))
print(result)
