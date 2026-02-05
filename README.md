# LangChain Models & Demos

A practical collection of LangChain patterns: LLM calls, chat models, embeddings, chains, tool calling, agents, structured outputs, and RAG (YouTube chatbot, loaders, retrievers, vector stores).

## Setup
- Python 3.10+ recommended.
- Install dependencies:
	```bash
	pip install -r requirements.txt
	```
- Configure provider keys as environment variables (set only what you use): `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `HF_TOKEN`, any local model paths.
- Use VS Code or Jupyter for notebooks.

## Quick Commands
```bash
# Smoke test
python test.py

# Chains
python chains/simple_chain.py

# Agent
python AIAgent/main.py

# Tool calling
python ToolCalling/tool_calling.py
```

## Repository Map
- [requirements.txt](requirements.txt) — Python dependencies.
- [steps.txt](steps.txt) — setup/run notes.
- [test.py](test.py) — smoke test / minimal demo runner.
- [1.LLMs/1_llm_demo.py](1.LLMs/1_llm_demo.py) — basic LLM invocation.
- [2.ChatModels](2.ChatModels) — chat model demos (Gemini, HF).
- [3.EmbeddingModels/3_embedding_hf_local.py](3.EmbeddingModels/3_embedding_hf_local.py) — local embedding example.
- [AIAgent](AIAgent) — agent pipeline:
	- [main.py](AIAgent/main.py) entry point.
	- [agent.py](AIAgent/agent.py) agent setup.
	- [llm.py](AIAgent/llm.py) model wrappers.
	- [tools.py](AIAgent/tools.py) tool definitions.
	- [prompt.py](AIAgent/prompt.py) prompt templates.
- [chains](chains) — chain patterns (simple, sequential, parallel, conditional).
- [parsed_output](parsed_output) — output parsing (string, JSON, Pydantic, structured output helpers).
- [structured_output/typed_dict.py](structured_output/typed_dict.py) — typed/structured responses.
- [ToolCalling](ToolCalling) — tool binding and execution demos.
- [Tools in LangChain](Tools%20in%20LangChain) — built-in and custom tool samples.
- [RAG](RAG) — retrieval-augmented generation examples:
	- [DocLoader](RAG/DocLoader) — text, CSV, PDF, directory, web loaders (sample data included).
	- [Retrievers](RAG/Retrievers) — retriever strategies (MMR, MQR, etc.).
	- [TextSplitters](RAG/TextSplitters) — splitting strategies and visualization notes.
	- [VectorStore](RAG/VectorStore) — Chroma vector store notebook.
	- [YoutubeChatbot_using_RAG.ipynb](RAG/YoutubeChatbot_using_RAG.ipynb) — end-to-end RAG chatbot demo.

## Notes
- Keep secrets in environment variables; do not commit keys.
- First runs may download models/embeddings; expect larger downloads for HF or local models.
- Notebooks assume Jupyter/VS Code support; install extensions if needed.


