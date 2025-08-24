from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini",
    api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base=os.getenv("OPENAI_BASE_URL"))

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')



if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)