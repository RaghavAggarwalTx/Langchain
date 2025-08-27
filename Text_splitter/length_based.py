from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(r'C:\Users\Raghav Agarwal\Desktop\Langchain_tut\Text_splitter\dl-curriculum.pdf')
docs=loader.load()
splitter=CharacterTextSplitter(chunk_size=200,
                               chunk_overlap=0,
                               separator='')

result=splitter.split_documents(docs)
print(result)

print(result[0])