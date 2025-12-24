# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# # model = ChatGoogleGenerativeAI(model='gemini-2.0-flash', temperature=0.8)
# # model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.8)

# model = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     api_version="v1",   # 👈 THIS IS THE KEY
#     temperature=0.8
# )

# result = model.invoke('tell me a poem on study')

# print(result.content)
# import google.generativeai as genai
# import os

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content("Write a short poem on studying")
# print(response.text)



from google import genai
import os

client = genai.Client(api_key=os.getenv("AIzaSyDc1djpq3GsqEOXethEdiyIUg0G9XGp5k4"))

response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents="Write a short poem on studying"
)

print(response.text)
