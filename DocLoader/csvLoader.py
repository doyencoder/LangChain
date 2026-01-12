from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

documents = loader.load()

print(documents[0].page_content)
print(documents[0].metadata)
print(documents[1].page_content)
print(documents[1].metadata)
print(f'Total Documents: {len(documents)}')