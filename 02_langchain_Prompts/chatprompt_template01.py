from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage


chat_template = ChatPromptTemplate([
    SystemMessage(content = "You are a helpful {domain} expert "),
    HumanMessage(content = "Explain in simple terms ,what is {topic}")
])



prompt = chat_template.invoke({'domain':'Cricket','topic':'dusra'})

print(prompt)

# yeh code run krege to run ho jauenga but the problem is 

# messages=[SystemMessage(content='You are a helpful {domain} expert ', additional_kwargs={},
#  response_metadata={}), HumanMessage(content='Explain in simple terms ,what is {topic}',
#   additional_kwargs={}, 
# response_metadata={})]

# domain{ expert} as it i schiz print ho gyi 
# similarly {topic} bhi 

# basically cricket and dusra fill hou hi nhi 
# so it thoda dismilar to ChatTemplate


# rather than giving this

# chat_template = ChatPromptTemplate([
#     SystemMessage(content = "You are a helpful {domain} expert "),
#     HumanMessage(content = "Explain in simple terms ,what is {topic}")
# ])


# you send tupples

