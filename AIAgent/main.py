from agent import agent_executor

if __name__ == "__main__":
    input_text = input("Enter your query: ")
    response = agent_executor.invoke({"input": input_text})
    print(response)