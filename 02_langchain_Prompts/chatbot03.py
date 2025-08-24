# now integrating Messages into show said to whom whwn you make
# chatbot it is imp to add messsage s



from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage , SystemMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI (model = "gemini-2.0-flash" , max_output_tokens = 200)
# model = ChatGoogleGenerativeAI()

chat_history =[
    SystemMessage(content = "You are a helpful AI asisstant")
]
while True:
    user_input = input ("you :")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break 
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI :  " ,result.content )

print(chat_history)
 
 
# now we solve our message is now labelled 


# [SystemMessage(content='You are a helpful AI asisstant', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi ', additional_kwargs={}, response_metadata={}), AIMessage(content='Hi there! How can I help you today?', additional_kwargs={}, response_metadata={}), HumanMessage(content='hi i am bhsuhan ', additional_kwargs={}, response_metadata={}), AIMessage(content="Hi Bhushan, it's nice to meet you! Is there anything I can do for you today?", additional_kwargs={}, response_metadata={}), HumanMessage(content='i am doing my msc in sc', additional_kwargs={}, response_metadata={}), AIMessage(content="That's great, Bhushan! MSc in Science is a broad field. Which area are you specializing in? Knowing that will help me understand how I can best assist you. \n\nFor example, are you studying:\n\n*   **Computer Science?**\n*   **Physics?**\n*   **Chemistry?**\n*   **Biology?**\n*   **Mathematics?**\n*   **Environmental Science?**\n*   Something else?\n\nLet me know! Good luck with your studies!", additional_kwargs={}, response_metadata={}), HumanMessage(content='what is my name ', additional_kwargs={}, response_metadata={}), AIMessage(content='Your name is Bhushan. You told me that earlier. 😊', additional_kwargs={}, response_metadata={}), HumanMessage(content='what a i am doing?', additional_kwargs={}, response_metadata={}), AIMessage(content="You told me you are doing your MSc in Science. Is there anything more specific you'd like me to recall about what you're doing? Perhaps you're working on a specific project, or studying a particular topic?", additional_kwargs={}, response_metadata={}), HumanMessage(content='exit', additional_kwargs={}, response_metadata={})]