from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.8, max_completion_tokens=10)

result = model.invoke('tell me a poem on study')

print(result.content)
