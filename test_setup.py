from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
c = Anthropic()
r = c.messages.create(
    model='claude-opus-4-7',
    max_tokens=100,
    messages=[{'role': 'user', 'content': 'Say hello in exactly 5 words.'}]
)
print(r.content[0].text)
print(f'Tokens: in={r.usage.input_tokens} out={r.usage.output_tokens}')
print('SETUP WORKS')