from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI (model = "gemini-2.0-flash" , max_output_tokens = 200)
# model = ChatGoogleGenerativeAI()

chat_history =[]
while True:
    user_input = input ("you :")
    chat_history.append(user_input)
    if user_input == "exit":
        break 
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI :  " ,result.content )

print(chat_history)



# now our chatbot has context but probelm is when chatbot is appending coversition in chat history the problem 
# it is short conversation but it doesnot telling which stament given by whom either by user or Ai
  
# ['hi iam bhushan ', "Hi Bhushan! It's nice to meet you. How can I help you today?", 'what is my name ', 'Your name is Bhushan. You told me that at the beginning of our conversation.', 'exit']