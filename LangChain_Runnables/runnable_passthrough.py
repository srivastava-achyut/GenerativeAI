from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# 1. Define Model and Parser
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite") # Note: use stable model names
parser = StrOutputParser()

# 2. Define Prompts
joke_prompt = PromptTemplate.from_template("Write a short joke about {topic}")
explain_prompt = PromptTemplate.from_template("Explain why this joke is funny: {joke}")

# 3. Define the Chain logic
# First, we generate the joke
joke_generation = joke_prompt | model | parser

# Then, we use RunnableParallel to branch the output
# 'joke' just passes the generated string through
# 'explanation' takes that same string and sends it to the second prompt
chain = joke_generation | RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": explain_prompt | model | parser
})

# 4. Execute
result = chain.invoke({"topic": "cricket"})

print(f"JOKE:\n{result['joke']}\n")
print(f"EXPLANATION:\n{result['explanation']}")