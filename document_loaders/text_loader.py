from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
loader=TextLoader(r'C:\Users\Raghav Agarwal\Desktop\Langchain_tut\document_loaders\cricket.txt',encoding='utf-8')
docs=loader.load()
print(docs)
print(type(docs))
print(len(docs))
print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)
# print(docs[0].metadata)

model = ChatOpenAI(model="gpt-4o-mini",
    api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"))

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)
parser=StrOutputParser()
chain=prompt|model|parser
print(chain.invoke({'poem':docs[0].page_content}))

