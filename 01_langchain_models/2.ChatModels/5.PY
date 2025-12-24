from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the LLM endpoint
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)


# Create the chat model wrapper
model = ChatHuggingFace(llm=llm, temperature= 0.5)

# Run the model
result = model.invoke("who is the current president of india in 2025")
print(result.content)
