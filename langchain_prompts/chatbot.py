from langchain_openai import ChatOpenAI
import os
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model="gpt-4o-mini",
    api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"))
chathistory=[
    SystemMessage(content='You are a helpful chat assistant')
]
while True:
    user_input=input("You :")
    chathistory.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result=model.invoke(chathistory)
    chathistory.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print(chathistory)