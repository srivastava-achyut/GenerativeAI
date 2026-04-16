from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnableSequence


load_dotenv()


prompt1 = PromptTemplate(
    template = 'Generate a 2 line tweet about \n {topic}',
    input_variables = ['topic']
)
prompt2 = PromptTemplate(
    template = 'Generate a 2 line LinkedIn post about \n {topic}',
    input_variables = ['topic']
)

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash-lite'
)

parser = StrOutputParser()
parallel_chain = RunnableParallel({
      'tweet':RunnableSequence(prompt1,model,parser),
       'linkedin':RunnableSequence(prompt2,model,parser)
})

result = parallel_chain.invoke({'topic':'AI'})
print(result)