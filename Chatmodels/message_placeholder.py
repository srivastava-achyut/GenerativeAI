from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
from langchain_core.messages import HumanMessage

chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagePlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history =[

]

# load chat history

with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt

prompt = chat_template.invoke({'chat_history':chat_history, 'query':HumanMessage(content='Where is my refund?')})
print(prompt)