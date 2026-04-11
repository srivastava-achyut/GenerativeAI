import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv



load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

chat_history =[
   
    SystemMessage(content="You are a helpful AI assistant ")
]
while True:
    user_input = input("Enter your query:")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break;
    response=model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ",response.content)

print(chat_history)

