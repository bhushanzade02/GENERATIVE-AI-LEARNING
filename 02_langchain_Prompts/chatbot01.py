# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# load_dotenv()

# model = ChatGoogleGenerativeAI (model = "gemini-2.0-flash" , max_output_tokens = 200)

# while True:
#     user_input = input ("you :")
#     if user_input == "exit":
#         break 
#     result = model.invoke(user_input)
#     print("AI :  " ,result.content )



# # in this code our chat bot wont have context for 2 or 90 grater then multiply by 10 




from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create the LLM endpoint
llm = HuggingFaceEndpoint(
    # repo_id="Qwen/Qwen2.5-1.5B-Instruct"
    #repo_id="mistralai/Mistral-7B-Instruct-v0.2"
    repo_id = "google/flan-t5-small",
    task="text-generation"
)

# Create the chat model wrapper
model = ChatHuggingFace(llm=llm, temperature= 0.5,max_=20 )

while True:
    user_input = input ("you :")
    if user_input == "exit":
        break 
    result = model.invoke(user_input)
    print("AI :  " ,result.content )

