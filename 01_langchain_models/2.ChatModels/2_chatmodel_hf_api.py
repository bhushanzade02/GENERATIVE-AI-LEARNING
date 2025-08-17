from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation"
)


# Create the chat model wrapper
model = ChatHuggingFace(llm=llm, temperature= 0.5)

# Run the model
result = model.invoke("Who is the president of India?")
print(result.content)
