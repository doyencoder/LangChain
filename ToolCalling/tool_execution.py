from tool_calling import result, messages, llm_with_tool
from tool import multiply


tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)
print(tool_result)

print(llm_with_tool.invoke(messages).content)

