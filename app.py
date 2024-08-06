import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables and configure API
load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function definitions (get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain, user_input) remain the same

def main():
    st.set_page_config(page_title="URDUx Doc-Chat", page_icon="👁‍🗨", layout="wide")
    
    # Custom CSS
    st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .st-bw {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("<h1 style='text-align: center; color: #2E86C1;'>URDUx Doc-Chat 👁‍🗨</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Upload PDFs, ask questions, and get instant answers!</p>", unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.markdown("<h2 style='text-align: center;'>📁 Document Upload</h2>", unsafe_allow_html=True)
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True, type="pdf")
        if st.button("Process Documents"):
            if pdf_docs:
                with st.spinner("Processing documents... This may take a moment."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Documents processed successfully!")
            else:
                st.warning("Please upload at least one PDF document.")

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<h3 style='color: #2E86C1;'>Ask Your Question</h3>", unsafe_allow_html=True)
        user_question = st.text_input("", placeholder="Type your question here...")
        if st.button("Get Answer"):
            if user_question:
                with st.spinner("Searching for the answer..."):
                    user_input(user_question)
            else:
                st.warning("Please enter a question.")

    with col2:
        st.markdown("<h3 style='color: #2E86C1;'>How to Use</h3>", unsafe_allow_html=True)
        st.markdown("""
        1. Upload your PDF documents using the sidebar.
        2. Click 'Process Documents' to analyze the content.
        3. Type your question in the input field.
        4. Click 'Get Answer' to receive a response.
        """)

    # Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Powered by URDUx | © 2024</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
