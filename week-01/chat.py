"""
chat.py — Stage 3: streaming multi-turn chat loop.

Maintains conversation history across turns. Streams response token-by-token. Type 'quit' to exit.
Stage 4 adds token accounting, stage 5 adds slash commands.
"""

from dotenv import load_dotenv
from anthropic import Anthropic

SYSTEM_PROMPT = "You are a research assistant for a data science student studying agentic AI."
MODEL = "claude-opus-4-7"


def main() -> None:
    load_dotenv()
    client = Anthropic()
    messages: list[dict] = []

    print("Chat started. Type 'quit' to exit.")

    try:
        while True:
            user_input = input("you: ").strip()

            if user_input.lower() == "quit":
                break

            if user_input == "":
                continue

            messages.append({"role": "user", "content": user_input})

            print("claude: ", end="", flush=True)
            with client.messages.stream(
                model=MODEL,
                system=SYSTEM_PROMPT,
                max_tokens=4096,
                messages=messages,
            ) as stream:
                for text_chunk in stream.text_stream:
                    print(text_chunk, end="", flush=True)
                print()
                final_message = stream.get_final_message()

            reply_text = final_message.content[0].text
            messages.append({"role": "assistant", "content": reply_text})

    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()