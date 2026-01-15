from langchain_classic.agents import create_react_agent
from langchain_classic.agents import AgentExecutor
from tools import tools
from llm import llm
from prompt import prompt

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)
