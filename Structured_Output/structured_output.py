from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite");

class Review(TypedDict):
    summary:str
    sentiment:str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("What is the capital of India?")

print(result)
