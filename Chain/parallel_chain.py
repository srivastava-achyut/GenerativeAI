from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
)
model2= ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
)

prompt1 = PromptTemplate(
    template="Generate a short and simple notes based on the text {text}",
    input_variables =['text']
)

prompt2 = PromptTemplate(
    template="Generate a 5 short question answer from the following text\n {text} ",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="merge the provided notes and quiz into a single document\n notes -> {notes} and quiz -> {quiz}",
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain
text ="""
      If you prefer a narrative format for your quiz material, here is an overview of cryptography written in standard prose.

Cryptography is the mathematical science of securing information so that it remains private and untampered with during storage or transmission. It operates on the fundamental principle of transforming readable information, known as plaintext, into an unreadable format called ciphertext through a process labeled encryption. To return this scrambled data to its original form, a specific piece of information called a key must be used during decryption. Modern cryptography is built upon the four pillars of confidentiality, integrity, authentication, and non-repudiation, ensuring that data is not only kept secret but also verified as genuine and unedited.

There are two primary methods of encryption used in digital systems today. Symmetric encryption relies on a single shared key that both the sender and the receiver must possess to lock and unlock the data. While this method is extremely fast and efficient for processing large amounts of information, it presents a significant security challenge regarding how to safely share the secret key without it being intercepted. In contrast, asymmetric encryption, or public-key cryptography, solves this problem by using a mathematically linked pair of keys. A public key is made available to the world for encryption, while a corresponding private key is held exclusively by the recipient for decryption. This system allows two parties to communicate securely even if they have never met or exchanged a secret key beforehand.

Beyond encryption, cryptography utilizes one-way functions known as hashing to protect data integrity. A hash function takes an input of any size and produces a unique, fixed-length string of characters that acts as a digital fingerprint. Because hashing is computationally impossible to reverse, it is used to verify that a file or message has not been altered; if even a single character in the original document is changed, the resulting hash will be entirely different. These concepts form the backbone of modern digital life, powering everything from secure web browsing via HTTPS to the verification of digital signatures and the immutable ledgers of blockchain technology.
"""
result =  chain.invoke({'text':text})

print(result)


