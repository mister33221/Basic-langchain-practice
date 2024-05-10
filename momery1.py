from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
import keys

key=keys.get_key("OPENAI_KEY")

llm = ChatOpenAI(api_key=key)

conversation = ConversationChain(llm=llm, verbose=True)

output = conversation.predict(input="Hello there, I'm kai, how are you?")
print(output)


output = conversation.predict(input="Recently, I've been feeling a bit down, do you have any advice?")
print(output)

# 他每一次的回答，都會包含之前的對話內容，使得對話更加連貫。
# 另外還有一個 ConversationBufferMemory，可以多研究一下
output = conversation.predict(input="Do you know my name and what I feel?")
print(output)
