from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from typing import TypedDict

# Load HF_TOKEN from .env
load_dotenv()

# -------------------------------
# 1. Define Structured Schema
# -------------------------------
class Person(TypedDict):
    name: str
    age: int
    city: str

# -------------------------------
# 2. Initialize Hugging Face LLM
# -------------------------------
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# -------------------------------
# 3. Create Structured Model
# -------------------------------
structured_model = model.with_structured_output(Person)

# -------------------------------
# 4. Invoke the Model
# -------------------------------
result = structured_model.invoke(
    "Generate the name, age (must be > 18), and city of a fictional Sri Lankan person."
)

# -------------------------------
# 5. Print Result
# -------------------------------
print(result)
