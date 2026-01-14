from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Paris is the capital of France.",
    "Berlin is the capital of Germany.",
    "New Delhi is the capital of India.",
]

docs = [Document(page_content=t) for t in texts]

vectorstore = FAISS.from_documents(docs, embeddings)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

results = retriever.invoke("What is the capital of Berlin?")
for d in results:
    print(d.page_content)
