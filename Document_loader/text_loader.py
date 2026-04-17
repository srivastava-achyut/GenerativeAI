from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

prompt = PromptTemplate(
    template = "write a summary for the following poem -\n {poem}",
    input_variables = ['poem']
)

parser = StrOutputParser()
loader  = TextLoader("cricket.txt",encoding='utf-8');


documents  = loader.load()
print(documents)

# print(type(documents))
# print(len(documents))
# print(documents[0].page_content)
# print(documents[0].metadata)

chain = prompt | model | parser
result = chain.invoke({'poem':documents[0].page_content})
print(result)