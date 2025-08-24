# we dont adding prmpt templat into this file we are 
#getiing prompt from json file thru template = load_prompt('template.json') 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate ,load_prompt


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

st.header("Reserach TOOl")

paper_input = st.selectbox("select research paper",["word2vec",'bert','difuusion models'])
style_input = st.selectbox( "select Explanation Style",['beginerr friendly','Techincal'])
length_input= st.selectbox("select explanation lenght",['short 1 - paragraphs','mdeium 3-5 paragraphs '])

#after creating json file callin go this file

template = load_prompt('template.json')

prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
    print(result.content)  