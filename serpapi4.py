# pip install numexpr

import os
from langchain_openai import ChatOpenAI
from langchain.agents import load_tools
# initialize_agent好像快要被棄用了，要改用甚麼再趕快去看看
from langchain.agents import initialize_agent
from langchain.agents import AgentType
import get_key

serpapi_key = get_key.get_key("SERPAPI_API_KEY")
openai_key = get_key.get_key("OPENAI_KEY")

# TODO 需要再去閱讀甚麼是 SerpAPI api，功能是甚麼及該如何使用。
os.environ["SERPAPI_API_KEY"] = serpapi_key
llm = ChatOpenAI(api_key=openai_key)

tools = load_tools(["serpapi", "llm-math"], llm=llm) 

# verbose=True 表示在運行過程中會顯示更多的信息，如處理過程、錯誤等。
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent.run("請問柯文哲最近有甚麼新聞?"))

