from langchain_community.retrievers.wikipedia import WikipediaRetriever

retriever = WikipediaRetriever(top_k=5, language="en", summarize=True)

query = "What is the capital of France?"
results = retriever.invoke(query)

for idx, result in enumerate(results):
    print(f"Result {idx + 1}:\n{result.page_content}\n")
