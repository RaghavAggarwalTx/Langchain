from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model=ChatOpenAI(model="gpt-4o-mini",
    api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"))

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about Langchain')
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)