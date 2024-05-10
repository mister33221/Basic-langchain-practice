# ChatOpenAI is a class that can be used to interact with OpenAI's chat models. It has many parameters that can be used, which can be found [here](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.base.ChatOpenAI.html). The parameters include openai_api_key: Optional[SecretStr] = None (alias 'api_key') which is the OpenAI API Key that needs to be provided, and model: Optional[str] = None which is the model to be used. The types of models that can be used can be found [here](https://platform.openai.com/settings/organization/limits). The invoke method of ChatOpenAI can be used to pass in a question and get an answer.
from langchain_openai import ChatOpenAI
# ChatProptTemplate is a class that can be used to create a chat prompt template. It has many parameters that can be used, which can be found [here](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.ChatPromptTemplate.html). The from_messages method of ChatPromptTemplate can be used to create a chat prompt template from a list of messages.
from langchain_core.prompts import ChatPromptTemplate
# The open ai response can be parsed using the StrOutputParser class from the langchain_core.output_parsers module.
from langchain_core.output_parsers import StrOutputParser
import keys

key=keys.get_key("OPENAI_KEY")

# Set a predefined system template
system_template = "You are a world class technical documentation writer."
# Set the user input
human_input = (
    "Please write a technical document for a software system structure document."
)

# Create a chat prompt template from the system template and user input
prompt = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", {input})]
)

# Put your chat open ai basic properties here, like the api key, which model to use, etc.
llm = ChatOpenAI(api_key=key)

# Create an output parser, it will parse the output from the model
output_parser = StrOutputParser()

# 這表示先將問題傳入 prompt，再將 prompt 的回答傳入 llm，最後將 llm 的回答傳入 output_parser
chain = prompt | llm | output_parser

# Print the response from the model
print(chain.invoke({"input": human_input}))
