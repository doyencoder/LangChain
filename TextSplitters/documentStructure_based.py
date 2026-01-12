# for splitting Markdown files based on headers
from langchain_text_splitters import MarkdownHeaderTextSplitter

text = """
# Deep Learning Curriculum

## Introduction
This course covers fundamentals of DL.

## CNN
Convolutional Neural Networks are used in vision.

### ResNet
Residual networks solve vanishing gradients.
"""

headers = [
    ("#", "H1"),
    ("##", "H2"),
    ("###", "H3"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers)

docs = splitter.split_text(text)
for d in docs:
    print(d.metadata, "\n", d.page_content, "\n---")

# for splitting Python code files
from langchain_text_splitters import PythonCodeTextSplitter

with open("textStructure_based.py", "r", encoding="utf-8") as f:
    code = f.read()

splitter = PythonCodeTextSplitter(
    chunk_size=300,
    chunk_overlap=30
)

chunks = splitter.split_text(code)

for i, c in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---\n")
    print(c)
