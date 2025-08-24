from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
import os

load_dotenv()

# Initialize model
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPEN_API_KEY"),   # make sure env var name is correct
    temperature=0.4,
    openai_api_base=os.getenv("OPENAI_BASE_URL")
)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text.\n{text}',
    input_variables=['text']
)

parser = StrOutputParser()

# Chain steps
to_summary_input = RunnableLambda(lambda x: {"text": x})

chain = template1 | model | parser | to_summary_input | template2 | model | parser

# Run
result = chain.invoke({'topic': 'black hole'})

print(result)
