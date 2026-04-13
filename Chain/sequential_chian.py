from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a detailed report on {topic}',
    input_variables =['topic']
)
prompt2= PromptTemplate(
    template = 'Write a 5 pointer summary of a given topic\n {text}',
    input_variables=['text']
)
model = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
)

parser = StrOutputParser()

chain1 = prompt1 | model | parser |prompt2 | model | parser
result = chain1.invoke({'topic':"Deforestation"})

print(result)
