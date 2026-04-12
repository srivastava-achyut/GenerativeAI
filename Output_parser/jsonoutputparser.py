import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser # Use JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite", # Note: use a released model like 1.5-flash for stability
    temperature=1.0
)

# Initialize the parser
parser = JsonOutputParser()

# Define the Template
template = PromptTemplate(
    template="Give me a fictional name, age, and city of a fictional person.\n{format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

# Construct the Chain
# This tells LangChain: Format Prompt -> Send to Gemini -> Parse result to JSON
chain = template | model | parser

# Invoke the chain
# result will now be a REAL Python Dictionary {}
result = chain.invoke({})

print(type(result)) # Output: <class 'dict'>
print(result)
print(f"Name: {result['name']}") # You can access keys directly!