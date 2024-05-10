import os
import get_key
from langchain_community.utilities import SerpAPIWrapper

key=get_key.get_key("SERPAPI_API_KEY")

# TODO 需要再去閱讀甚麼是 SerpAPI api，功能是甚麼及該如何使用。
os.environ["SERPAPI_API_KEY"] = key

search = SerpAPIWrapper()
print(search.run("你是誰?"))





