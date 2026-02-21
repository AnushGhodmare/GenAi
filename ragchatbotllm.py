import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama

#page config 
st.set_page_config(page_title="C++ RAG Chatbot")
st.title("C++ RAG Chatbot")
st.write("Ask any question related to C++ introduction")

@st.cache_resource
def load_vectorstore():
    loader = TextLoader("C++_Introduction.txt",encoding="UTF-8")
    documents = loader.load()

    #Split Text
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
    )
    final_documents = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = FAISS.from_documents(final_documents, embeddings)
    return db

db = load_vectorstore()

llm = Ollama(model="gemma2:2b")
user_question=st.text_input("Enter your question for c++")
if user_question:
    with st.spinner("thinking...."):
        docs = db.similarity_search(user_question)
        context = "\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer the question using only the context below

        context:
        {context}

        Question:
        {user_question}

        Answer:
        """
        response = llm.invoke(prompt)
        
        st.subheader("Answer")
        st.write(response)
