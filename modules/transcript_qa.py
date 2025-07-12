from langchain_community.llms import LlamaCpp
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from config import TRANSCRIPT_PATH, VECTOR_DB_PATH

def build_vectorstore():
    all_docs = []
    for file in os.listdir(TRANSCRIPT_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(TRANSCRIPT_PATH, file))
            all_docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(all_docs)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(VECTOR_DB_PATH)

def get_transcript_qa_chain():
    db = FAISS.load_local(
        folder_path=VECTOR_DB_PATH,
        embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2"),
        allow_dangerous_deserialization=True
    )

    llm = LlamaCpp(
        model_path="./models/phi-2.Q4_K_M.gguf",
        n_ctx=2048,
        temperature=0.6,
        max_tokens=512,
        top_p=0.95,
        repeat_penalty=1.1,
        verbose=True
    )

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    return qa_chain
