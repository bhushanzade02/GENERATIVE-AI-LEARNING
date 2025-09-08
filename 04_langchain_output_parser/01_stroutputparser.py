from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

# 1st prompt - > detailed report
template1 =PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variable =['topic']
)
#2nd prompt - > summary
template2 = PromptTemplate(
    template ="write a 5 line summary on the following text. /n {text}",
    input_variables =['text']
)

prompt1 = template1.invoke({'topic' : 'black hole'})

result = model.invoke(prompt1)
print(result.content)
prompt2 = template2.invoke({'text':result.content})

result2 = model.invoke(prompt2)

print(result2.content)