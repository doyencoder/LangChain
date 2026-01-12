from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

prompt1 = PromptTemplate(
    template='Generate a detailed report about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following report in bullet points:\n{report}',
    input_variables=['report']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Indian Institute of Technology Banaras Hindu University (IIT BHU)'})

print(result)

chain.get_graph().print_ascii() # To visualize the chain structure(pipelines)