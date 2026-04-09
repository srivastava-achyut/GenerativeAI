# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Hum wahi model use karenge jo aapke list mein present tha
# # 'gemini-2.0-flash-lite' ka quota usually zyada hota hai
# model = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash-lite", 
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

# try:
#     print("Sending request...")
#     result = model.invoke("What is the capital of India?")
#     print("Success! Output:")
#     print(result.content)
# except Exception as e:
#     print(f"Error: {e}")


# from google import genai    this is direct google sdk use technique not langchian

# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="What is the capital of India?"
# )
# print(response.text)

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

# os.environ["GOOGLE_API_KEY"] = ""

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
response = model.invoke("What is the capital of India")
print(response.content)