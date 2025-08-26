from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import openai
import os
loader=TextLoader('doc.txt')
documents=loader.load()

text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs=text_splitter.split_documents(documents)

vectorstore=FAISS.from_documents(docs,OpenAIEmbeddings())
retriever=vectorstore.as_retriever()

query="What are the key takeaways from the document ?"
retrieved_docs=retriever.get_relevant_documents(query)

retrieved_text="\n".join([doc.page_content for doc in retrieved_docs])

llms=openai(model_name='gpt-4o-mini',
    api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"),
    temperature=0.7)

prompt=f"Based on the following text,answer  the question:{query}\n\n{retrieved_docs}"