from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from tool import multiply  # import from other file
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

# bind the external tool
llm_with_tool = llm.bind_tools([multiply])

# test direct call
# print(multiply.invoke({"a": 3, "b": 4}))