print("Hello Wolf.")

import requests
from dotenv import load_dotenv

load_dotenv()
# import agent
from langchain.agents import create_agent
# import tools
from langchain.tools import tool

@tool('get_weather', description="Return weather information for a given city", return_direct=False)
def get_weather(city:str):
    response = requests.get(f'https://wttr.in/{city}?format=j1')
    return response.json()

agent = create_agent(
    model='claude-haiku-5-5',
    tools=[get_weather],
    system_prompt='You are a helpful weather assistant, who always cracks jokes and humorous while remaining helpful.'
)

response = agent.invoke({
    'messages' : [
        {'role' : 'user', 'content' : 'What is the wather like in Bangkok Thailand ?'}
    ]
})

#print(response)
print(response['messages'][-1].text)