from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

template1 = PromptTemplate(
    template = 'Write a detailed review of the following product: {product_description}',
    input_variables = ['product_description']
)

template2 = PromptTemplate(
    template = 'Summarize the following review in one sentence: {review}',
    input_variables = ['review']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'product_description': 'Samsung Galaxy S24 Ultra smartphone with Snapdragon 8 Gen 3 processor, 5000mAh battery, S-Pen integration, and 200MP camera'})
print(result)