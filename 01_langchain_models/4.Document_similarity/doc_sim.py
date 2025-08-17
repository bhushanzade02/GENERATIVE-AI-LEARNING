from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding =GoogleGenerativeAIEmbeddings(model ="models/text-embedding-004")
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]



# query = "tell me about bhushan "
query = str(input("ask me about cicket "))
doc_embedding =embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)



scores = cosine_similarity([query_embedding],doc_embedding)[0]

index , score = sorted(list(enumerate(scores)),key = lambda x:x[1])[-1]



print(" ")
print(" ")
print("⚠️ WARNING: GOOGLE GEMINI PRO API. Ensure proper usage, rate limits, and API key security.")

print(" ")
#print(query)
print(documents[index])
print(" ")
print(" ")
print(" ")
print(" ")

print("similarity score is : ", score)