# from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv
# import os

# load_dotenv()

# # Ensure token is present
# if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
#     print("Error: Please set HUGGINGFACEHUB_API_TOKEN in your .env file")

# llm = HuggingFaceEndpoint(
#     repo_id="mistralai/Mistral-Small-4-119B-2603",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model = ChatHuggingFace(llm=llm)

# # Define the Templates
# template1 = PromptTemplate.from_template("Write a detailed report on {topic}")
# template2 = PromptTemplate.from_template("Write a 5 line summary on the following text report: {text}")

# # Chain 1: Generate the report
# chain1 = template1 | model
# result1 = chain1.invoke({"topic": "black hole"})

# # Chain 2: Summarize the report content
# chain2 = template2 | model
# result2 = chain2.invoke({"text": result1.content})

# print("--- SUMMARY ---")
# print(result2.content)


## using the gemini api key

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize the Gemini model
# Note: google_api_key will automatically look for GOOGLE_API_KEY in your .env
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", 
    temperature=1.0
)

# Define the Templates
template1 = PromptTemplate.from_template("Write a detailed report on {topic}")
template2 = PromptTemplate.from_template("Write a 5 line summary on the following text report: {text}")

# Define the Parser
parser = StrOutputParser()

# Chain 1: Topic -> Report -> String
chain1 = template1 | model | parser

# Chain 2: Text -> Summary -> String
chain2 = template2 | model | parser
chain=chain1|chain2
# Execution

result = chain.invoke({"topic": "electrical engineering"})

print("Generating Summary...")


print("\n--- FINAL SUMMARY ---")
print(result)