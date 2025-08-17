#add dynamic template 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

st.header("Reserach TOOl")

paper_input = st.selectbox("select research paper",["word2vec",'bert','difuusion models'])
style_input = st.selectbox( "select Explanation Style",['beginerr friendly','Techincal'])
length_input= st.selectbox("select explanation lenght",['short 1 - paragraphs','mdeium 3-5 paragraphs '])


#template
template = PromptTemplate(
    template = """ 
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length: {length_input}

Mathematical Details:

Include relevant mathematical equations if present in the paper.

Explain the mathematical concepts using simple, intuitive code snippets where applicable.

Analogies:

Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.""",
input_variables = ['paper_input','style_input', 'length_input'],
validate_template = True 
 )

# fill the placeholders

prompt = template.invoke({
    'paper_input' : paper_input,
    'style_input' : style_input,
    'length_input' : length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
    print(result.content)  