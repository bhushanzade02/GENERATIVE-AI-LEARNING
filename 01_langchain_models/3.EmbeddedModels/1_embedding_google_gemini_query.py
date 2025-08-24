from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004",dimensions =32)

result = embeddings.embed_query("delhi is capital of india")

print(str(result))  # This will print a list of floats (the embedding vector)

