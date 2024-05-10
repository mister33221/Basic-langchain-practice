import os
from langchain_community.utilities import SerpAPIWrapper
import get_key

key=get_key.get_key("SERPAPI_API_KEY")

# TODO 需要再去閱讀甚麼是 SerpAPI api，功能是甚麼及該如何使用。
os.environ["SERPAPI_API_KEY"] = key

params = {
    "engine": "bing",
    "gl": "us",
    "hl": "en",
}
search = SerpAPIWrapper(params=params)

print(search.run("What is the capital of Taiwan?"))


