import requests
from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()

model = init_chat_model(
    model='claude-haiku-5-5',
)

conversation = [
    SystemMessage('You are a helpful asssistant for question regrading programming.'),
    HumanMessage('What is python ?'),
    AIMessage('Python is an interpreted programming language.'),
    HumanMessage('What was it released ?')
]

response = model.invoke(conversation)

print(response)
print(response.text)
