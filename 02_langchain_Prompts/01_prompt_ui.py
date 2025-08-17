from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

st.header("Reserach TOOl")


user_input = st.text_input('Enter your prompt')

if st.button("Summarize"):
    result = model.invoke(user_input)
    st.write(result.content)

# this static prompt if you want info about other rerach paper then you have to give input (prompt) 
# staic prompt is not used as much beacuse you are giving more control to user