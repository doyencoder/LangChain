from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

# Sample documents
texts = [
    "LangChain makes it easy to work with LLMs.",
    "LangChain is used to build LLM based applications.",
    "Chroma is used to store and search document embeddings.",
    "Embeddings are vector representations of text.",
    "MMR helps you get diverse results when doing similarity search.",
    "LangChain supports Chroma, FAISS, Pinecone, and more.",
]

docs = [Document(page_content=t) for t in texts]

vectorstore = FAISS.from_documents(docs, embeddings)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0.0}
)

query = "What is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)