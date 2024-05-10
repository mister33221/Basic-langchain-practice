# This is not working yet.

# from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
import keys

key=keys.get_key("OPENAI_KEY")

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=key,
)

prompt = ChatPromptTemplate.from_messages(
    [("system", "What are everyone's favorite colors:\n\n{context}")]
)

docs = [
    Document(page_content="Jesse loves red but not yellow"),
    Document(page_content="Jamal loves green but not as much as he loves orange"),
]

chain = create_stuff_documents_chain(llm, prompt)

print(chain.invoke({"context": docs}))
