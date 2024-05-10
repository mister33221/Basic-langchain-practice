import os
import keys
from langchain_community.utilities import SerpAPIWrapper

key=keys.get_key("SERPAPI_API_KEY")

# TODO 需要再去閱讀甚麼是 SerpAPI api，功能是甚麼及該如何使用。
os.environ["SERPAPI_API_KEY"] = key

search = SerpAPIWrapper()
print(search.run("你是誰?"))





