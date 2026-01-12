from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=100,
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser(json_schema = {
    "title": "Facts",
    "type": "object",
    "properties": {
        "fact1": {"type": "string", "description": "First fact"},
        "fact2": {"type": "string", "description": "Second fact"},
        "fact3": {"type": "string", "description": "Third fact"},
    },
    "required": ["fact1", "fact2", "fact3"]
})

template = PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic': 'The Eiffel Tower'})
print(result)