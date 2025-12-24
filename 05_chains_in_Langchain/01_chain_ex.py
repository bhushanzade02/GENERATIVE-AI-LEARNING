

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = "Generate 5 intresting facts about {topic}",
    input_variables = ['topic']
)

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    temperature= 0.5,
    max_new_tokens=150
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


chain = prompt | model | parser


result = chain.invoke({"topic":"cricket"})
print(result)


print(chain)



# chain.get_graph().print_ascii()

