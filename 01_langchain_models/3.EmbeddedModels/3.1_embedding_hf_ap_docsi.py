from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()


embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents= ['delhi is capital of india','mumbai is capital of mh','kolkata is capital of wb']
vector = embedding.embed_documents(documents)
print(str(vector))