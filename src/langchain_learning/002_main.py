import requests
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()

model = init_chat_model(
    model='claude-haiku-5-5',
)

for chunk in model.stream('What is python ?'):
    print(chunk.text, end='', flush=True)
