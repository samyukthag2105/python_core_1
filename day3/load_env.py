import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
hf_key = os.getenv("HF_API_KEY")

if openai_key:
    print("OpenAI key loaded successfully!")
else:
    print("OpenAI key not found.")

if hf_key:
    print("Hugging Face key loaded successfully!")
else:
    print("Hugging Face key not found.")
    