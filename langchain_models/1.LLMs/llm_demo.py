from langchain_openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
llm= OpenAI(
    model="gpt-3.5-turbo",
    openai_api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL")
)  
reulst=llm.invoke('What is the captial of india ')
print(reulst)