import os
from dotenv import load_dotenv
# Correct imports for Gemini and Output Parsers
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StructuredOutputParser
from langchain_core.output_parsers import ResponseSchema
from langchain_core.prompts import PromptTemplate



# 1. Load your GOOGLE_API_KEY from .env
load_dotenv()

# 2. Initialize Gemini 1.5 Flash (or Pro)
# Gemini 1.5 Flash is great for quick, structured tasks
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.1,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# 3. Define the response schema
response_schemas = [
    ResponseSchema(name="answer", description="The direct answer to the user's question"),
    ResponseSchema(name="confidence", description="How confident the model is (0.0 to 1.0)"),
    ResponseSchema(name="reasoning", description="Brief logic behind the answer")
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
format_instructions = output_parser.get_format_instructions()

# 4. Create the Prompt Template
template = """
You are a precise technical assistant. 

{format_instructions}

Question: {question}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["question"],
    partial_variables={"format_instructions": format_instructions}
)

# 5. Build the Chain (LCEL)
chain = prompt | llm | output_parser

# 6. Run the script
if __name__ == "__main__":
    try:
        query = "What causes the aurora borealis?"
        result = chain.invoke({"question": query})
        
        print("\n--- Gemini Structured Response ---")
        print(f"Answer: {result['answer']}")
        print(f"Confidence: {result['confidence']}")
        print(f"Reasoning: {result['reasoning']}")
        
    except Exception as e:
        print(f"An error occurred: {e}")