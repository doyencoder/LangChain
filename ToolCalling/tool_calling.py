from tool_binding import llm_with_tool
from langchain_core.messages import HumanMessage

query = HumanMessage('can you multiply 3 with 1000')
messages = [query]
result = llm_with_tool.invoke(messages)
messages.append(result)

# print(messages)   


