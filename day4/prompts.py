import json


def ask_llm(prompt, system=None):
    """
    Simulated LLM.
    """

    print("=" * 50)

    if system:
        print("SYSTEM:")
        print(system)

    print("\nPROMPT:")
    print(prompt)

    fake_response = """
    {
        "sentiment": "Positive",
        "reason": "The customer enjoyed the experience."
    }
    """

    return json.loads(fake_response)



print("\nZERO-SHOT")

result = ask_llm(
    "Classify the sentiment of: The food was delicious and the service was excellent."
)

print(result)


print("\nFEW-SHOT")

result = ask_llm("""
Example 1

Review:
The food was terrible.

Sentiment:
Negative

Example 2

Review:
The waiter was very friendly.

Sentiment:
Positive

Now classify:

The food was delicious and the service was excellent.
""")

print(result)


print("\nCHAIN OF THOUGHT")

result = ask_llm(
"Think step by step before deciding the sentiment."
)

print(result)

print("\nSYSTEM PROMPT")

result = ask_llm(
    prompt="Classify the review.",
    system="You are a professional restaurant review analyst."
)

print(result)


print("\nSTRUCTURED OUTPUT")

result = ask_llm(
    "Reply only in JSON with sentiment and reason."
)

print(result)
