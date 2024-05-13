# %pip install --upgrade --quiet  docx2txt --user
import keys
from langchain_community.document_loaders import Docx2txtLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain

key = keys.get_key("OPENAI_KEY")
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=key,
)

# 路徑是相對於你執行這個程式時的terminal的位置
docx2txt_loader = Docx2txtLoader(
    "./doc_gpt/example_data/富邦_資產總覽功能清單_0312.docx"
)
data = docx2txt_loader.load()
docs = [
    Document(page_content=data[0].page_content),
]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "{context}"),
        ("user", "請問中台運作監控系統有哪些重要的功能? 請使用繁體中文回答我"),
    ]
)

chain = create_stuff_documents_chain(llm, prompt)

# 這裡的變數名稱必須使用 context
print(chain.invoke({"context": docs}))


