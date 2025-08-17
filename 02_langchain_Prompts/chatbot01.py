from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI (model = "gemini-2.0-flash" , max_output_tokens = 200)

while True:
    user_input = input ("you :")
    if user_input == "exit":
        break 
    result = model.invoke(user_input)
    print("AI :  " ,result.content )



# in this code our chat bot wont have context for 2 or 90 grater then multiply by 10 exmpale