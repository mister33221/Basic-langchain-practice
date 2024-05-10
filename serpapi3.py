import os
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents import Tool
import get_key

key=get_key.get_key("SERPAPI_API_KEY")

# SerpAPI 是一個實時 API，用於訪問 Google 搜索結果。
# 它處理代理、解決驗證碼，並為您解析所有豐富的結構化數據1。
# 這個工具不僅僅是一個搜索爬取工具，
# 它還是一個通往搜索引擎結果中隱藏的有價值洞察的門戶。
# 無論您是 SEO 專家、市場研究員還是競爭情報專家，
# SerpAPI 都能讓您做出數據驅動的決策，獲得戰略優勢2。
os.environ["SERPAPI_API_KEY"] = key

params = {
    # "engine": "bing",
    "engine": "google",
    "gl": "us",
    "hl": "en",
}
search = SerpAPIWrapper(params=params)

repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=search.run,
)

print(repl_tool.run("中國是中華人民共和國還是中華民國?"))

