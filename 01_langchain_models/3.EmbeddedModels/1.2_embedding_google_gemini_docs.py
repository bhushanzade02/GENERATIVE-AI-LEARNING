from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004",dimensions=32)

documents = ["delhi is caital of india","mumbai is capital of maharashtra","paris is capital of france"]

result = embeddings.embed_documents(documents)

print(str(result))  
