from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL")
)
result=model.invoke("What is the capital of india")
print(result.content)