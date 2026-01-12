from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model='gemini-3-flash-preview')

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=100,
)

model2 = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template='Generate a short note on {report}',
    input_variables=['report']
)

prompt2 = PromptTemplate(
    template='Generate 2 quiz questions from the following report:\n{report}',
    input_variables=['report']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz questions into a single document:\nNotes: {notes}\nQuiz Questions: {quiz_questions}',
    input_variables=['notes', 'quiz_questions']
)

parser = StrOutputParser()

parallel_chain =  RunnableParallel(
    {
        'notes': prompt1 | model1 | parser,
        'quiz_questions': prompt2 | model1 | parser
    }
)
merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain

text = """
    The Indian Institute of Technology (IIT) BHU Varanasi, 
    established in 1919 as the Banaras Engineering College, is one of the 
    oldest technical institutions in India. It became an IIT in 2012 and 
    is located in Varanasi, Uttar Pradesh. The institute offers undergraduate, 
    postgraduate, and doctoral programs in various engineering and technology 
    disciplines. IIT BHU is known for its strong emphasis on research and innovation, 
    with numerous research centers and collaborations with industries. 
    The campus is equipped with modern facilities, including state-of-the-art 
    laboratories, libraries, and hostels. IIT BHU has a vibrant student community
    with various clubs and organizations that promote extracurricular activities 
    and cultural events. The i  nstitute has produced many notable alumni who have 
    made significant contributions in academia, industry, and entrepreneurship globally.
 """

result = chain.invoke({'report': text})

print(result)

chain.get_graph().print_ascii() # To visualize the chain structure(pipelines)