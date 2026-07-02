import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="hf-inference",
    api_key=os.getenv("HF_API_KEY"),
)

try:
    completion = client.chat.completions.create(
        model="google/gemma-3-1b-it",
        messages=[
            {
                "role": "user",
                "content": "Explain RAG in one sentence."
            }
        ],
        max_tokens=50,
    )

    print("\nLLM Response:\n")
    print(completion.choices[0].message.content)

except Exception as e:
    print("Error:", e)
    