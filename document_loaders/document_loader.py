from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
loader=PyPDFLoader(r'C:\Users\Raghav Agarwal\Desktop\Langchain_tut\document_loaders\dl-curriculum.pdf')
docs=loader.load()
print(docs)
print(type(docs))
print(len(docs))
print(docs[0])
print(type(docs[0]))
print(docs[0].page_content)
print(docs[0].metadata)

# model = ChatOpenAI(model="gpt-4o-mini",
#     api_key=os.getenv("OPEN_API_KEY"),
#     openai_api_base=os.getenv("OPENAI_BASE_URL"))