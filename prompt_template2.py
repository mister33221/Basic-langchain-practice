# Most LLM applicatoin do not pass user input directly into an LLM.
# Usually thay will add the user input to a larger pirce of text, called a propt
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import keys

key=keys.get_key("OPENAI_KEY")

# Create a prompt template Way 2
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)

print(prompt.format(product="colorful hats"))

llm = ChatOpenAI(api_key=key)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print(chain.invoke({"product": "colorful hats"}))
