from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model= "sentence-transformers/all-MiniLM-L6-v2")


documents = ["delhi is capital of india",
"kolkata is capital of india",
"paris is capital of france"]


vector = embedding.embed_documents(documents)

print(str(vector))