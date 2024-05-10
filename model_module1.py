# 使用 langchain_openai 模組中的 ChatOpenAI 類別
from langchain_openai import ChatOpenAI
import get_key

key=get_key.get_key("OPENAI_KEY")

# ChatOpenAI 有很多參數可以使用，可以參考[這裡](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html)
# openai_api_key: Optional[SecretStr] = None (alias 'api_key') 要放入 OpenAI API Key
# model: Optional[str] = None 要使用的模型，類型種類可以參考[這裡](https://platform.openai.com/settings/organization/limits)
llm = ChatOpenAI(api_key=key)

# 使用 ChatOpenAI 的 invoke 方法，可以將問題傳入並取得回答
print(llm.invoke("how can langsmith help with testing?"))

