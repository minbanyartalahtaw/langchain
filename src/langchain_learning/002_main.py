import requests
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.tools import tool

load_dotenv()

model = init_chat_model(
    model='claude-haiku-5-5',
)

response = model.invoke('What is the python ?')

print(response)
print(response.text)
