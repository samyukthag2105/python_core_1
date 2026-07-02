import requests

try:
    response = requests.get("https://huggingface.co")
    print("Status:", response.status_code)
except Exception as e:
    print("Error:", e)
