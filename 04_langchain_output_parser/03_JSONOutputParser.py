from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = 'google/gemma-2-2b-it',
    task ='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template = "give me 5 facts about {topic} \n {format_instruction}",
    input_variables =['topic'],
    partial_variables ={'format_instruction':parser.get_format_instructions() }
)
""" 
# prompt =template.format()


# result = model.invoke(prompt)

# print(result.content)
#  print(result) 
# this will give unnecessary part 
# we want only content part so parse this into json paerser
#the it will give json schema


#SIMPLE  (NOT BY USINF CHAIN)
# final_result = parser.parse(result.content)
# print(final_result)
# print(final_result['name'])
# print(type(final_result))
"""

# ( BY USING CHAIN)
chain = template | model | parser


result = chain.invoke({'topic':'black hole'})

print(result)