import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

NUM_RUNS_TIMES = 5

# TODO: Fill this in!
# k shot은 지시와 함께 n개의 예시를 제공하는 것이다.
YOUR_SYSTEM_PROMPT = """
    You're a senior python developer who makes algorithms.
    Reverse the order of letters in the following word. I give you examples.
    
    example word: "httpstatus"
    result reversed word: "sutatsptth"

    example word: "success"
    result reversed word: "sseccus"
    
    example word: "hello world!"
    result reversed word: "!dlrow olleh"

    example word: "!@#$%^"
    result reversed word: "^%$#@!"

    example word: "Nintendo Switch! good!"
    result reversed word: "!doog !hctiwS odnetniN"
"""

USER_PROMPT = """
Reverse the order of letters in the following word. Only output the reversed word, no other text:

httpstatus
"""


EXPECTED_OUTPUT = "sutatsptth"

def test_your_prompt(system_prompt: str) -> bool:
    """Run the prompt up to NUM_RUNS_TIMES and return True if any output matches EXPECTED_OUTPUT.

    Prints "SUCCESS" when a match is found.
    """
    for idx in range(NUM_RUNS_TIMES):
        print(f"Running test {idx + 1} of {NUM_RUNS_TIMES}")
        response = chat(
            model="mistral-nemo:12b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": USER_PROMPT},
            ],
            options={"temperature": 0.5},
        )
        output_text = response.message.content.strip()
        if output_text.strip() == EXPECTED_OUTPUT.strip():
            print("SUCCESS")
            return True
        else:
            print(f"Expected output: {EXPECTED_OUTPUT}")
            print(f"Actual output: {output_text}")
    return False

if __name__ == "__main__":
    test_your_prompt(YOUR_SYSTEM_PROMPT)