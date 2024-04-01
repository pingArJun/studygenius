from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document

def split_text_q_gen(data):
    text_splitter = TokenTextSplitter(model_name="gpt-3.5-turbo-16k", chunk_size=10000, chunk_overlap=200)
    texts = text_splitter.split_text(data)
    docs = [Document(page_content=t) for t in texts]
    return docs

def split_text_q_answer(data):
    text_splitter = TokenTextSplitter(model_name="gpt-3.5-turbo", chunk_size=2000, chunk_overlap=200)
    texts = text_splitter.split_text(data)
    docs = [Document(page_content=t) for t in texts]
    return docs

def split_text_docs_vector(data):
    text_splitter = TokenTextSplitter(model_name="gpt-3.5-turbo", chunk_size=2000, chunk_overlap=200)
    docs = text_splitter.split_documents(data)
    return docs
