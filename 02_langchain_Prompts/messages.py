#  now who said to whom problem solved 
# [SystemMessage(content='You are a helpful assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='tell me a about Langchain', additional_kwargs={}, response_metadata={}), AIMessage(content="Okay, let's dive into Langchain!\n\n**What is Langchain?**\n\nLang", additional_kwargs={}, response_metadata={})]

from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash" , max_output_tokens = 20)

messages = [
    SystemMessage (content = "You are a helpful assistant"),
    HumanMessage (content = "tell me a about Langchain")
    
]
result = model.invoke(messages)
messages.append(AIMessage(content= result.content))
print(messages)
