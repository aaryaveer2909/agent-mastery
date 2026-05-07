"""
chat.py - Stage 1:single-turn hello world
Sends one message to Claude, prints the response and token usage.
"""

import os
from dotenv import load_dotenv
from anthropic import Anthropic

SYSTEM_PROMPT = "You are a research assistant for a data science student studying agentic AI."
MODEL = "claude-opus-4-7"

def main() -> None:
    load_dotenv()
    client = Anthropic()
    response=client.messages.create(
        model=MODEL,
        system=SYSTEM_PROMPT,
        max_tokens=1024,
        messages=[{
            "role": "user", "content": "In one sentence, what is a 10-k filing?"
        },])

    

    print(response.content[0].text)
    print(f"input: " ,(response.usage.input_tokens))
    print(f"output: " ,(response.usage.output_tokens))
    
if __name__ == "__main__":
    main()

