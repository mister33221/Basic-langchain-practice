# pip install pypdf --user
import keys
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import PyPDFLoader

key = keys.get_key("OPENAI_KEY")
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=key,
)

loader = PyPDFLoader("./doc_gpt/example_data/富邦_資產總覽功能清單_0312.pdf")
data = loader.load_and_split()

raw_text = ''
for page in data:
    raw_text += page.page_content

docs = [
    Document(page_content=raw_text),
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "{context}"),
        ("user", "這份資料裡面有甚麼資料?我可以使用這份資料來做甚麼?f請給我大綱。請使用繁體中文回答我"),
    ]
)

chain = create_stuff_documents_chain(llm, prompt)

# 這裡的變數名稱必須使用 context
print(chain.invoke({"context": docs}))


