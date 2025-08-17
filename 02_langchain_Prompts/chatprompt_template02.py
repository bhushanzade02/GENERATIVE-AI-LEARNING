from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([


    ('system' ,'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms ,what is {topic}')
   
])

prompt = chat_template.invoke({'domain':'Cricket','topic':'dusra'})

print(prompt)

# now the problem is solved 

# messages=[SystemMessage(content='You are a helpful Cricket expert', additional_kwargs={}, response_metadata={}), HumanMessage(content='Explain in simple terms ,what is dusra', additional_kwargs={}, response_metadata={})]


# placeholde rmein cricket and dusra ki value aa gyi hain 