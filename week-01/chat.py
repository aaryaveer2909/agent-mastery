"""
chat.py — Stage 2: multi-turn chat loop.

Maintains conversation history across turns. Type 'quit' to exit
stage 3 adds streaming, stage 4 adds token accounting, stage 5 adds slash commands
"""

from dotenv import load_dotenv
from anthropic import Anthropic

SYSTEM_PROMPT = "You are a research assistant for a data science student studying agentic AI."
MODEL = "claude-opus-4-7"


def main() -> None:
    load_dotenv()
    client = Anthropic()
    #intialized messages array: list of dictionaries
    messages: list[dict]= []

    print("Chat started. Type 'quit' to exit.")

    #multi turn chat loop that keeps memory until terminated
    try:
        while True:
            user_input = input("you: ")
            user_input=user_input.strip()

            if user_input.lower() == "quit":
                break

            if user_input == "":
                continue
            
            messages.append({"role": "user", "content": user_input})

            response= client.messages.create(
                model= MODEL,
                system= SYSTEM_PROMPT, 
                messages=messages,
                max_tokens=4096
            )

            reply_text = response.content[0].text

            messages.append({"role": "assistant", "content": reply_text})

            print(f"claude:  {reply_text}")

    except KeyboardInterrupt:
        print("\nExiting.")

            

if __name__ == "__main__":
    main()