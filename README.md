# URDUx Doc-Chat 👁‍🗨

URDUx Doc-Chat is a cutting-edge document interaction tool that leverages the power of AI to revolutionize how you extract information from PDF documents. Say goodbye to endless scrolling and hello to instant, accurate answers!

## 🚀 Features

- **PDF Processing**: Upload multiple PDFs and process them in seconds.
- **AI-Powered Q&A**: Ask questions about your documents and get detailed answers instantly.
- **Smart Context Understanding**: The AI understands document context, providing relevant and accurate responses.
- **User-Friendly Interface**: Simple, intuitive Streamlit-based UI for seamless interaction.
- **Google Generative AI Integration**: Harnesses the power of Google's latest AI models for superior performance.

## 🛠️ Technologies Used

- **Streamlit**: For the interactive web application
- **PyPDF2**: PDF processing
- **LangChain**: For building scalable AI/LLM apps and chatbots
- **Google Generative AI**: State-of-the-art language model
- **FAISS**: Efficient similarity search and clustering of dense vectors

## 🚦 Prerequisites

- Python 3.7+
- Google API key for Generative AI

## 🚀 Quick Start

1. Install dependencies:
`pip install -r requirements.txt`

3. Set your Google API key in a `.env` file:
`GOOGLE_API_KEY=your_api_key_here`

4. Run the app:
`streamlit run app.py`

5. Upload PDFs, process them, and start asking questions!


## 🎯 How It Works

1. **Document Upload**: Users upload PDF files through the Streamlit interface.
2. **Text Extraction**: PyPDF2 extracts text from the uploaded PDFs.
3. **Text Chunking**: The extracted text is split into manageable chunks.
4. **Embedding Generation**: Google's Generative AI creates embeddings for the text chunks.
5. **Vector Storage**: FAISS stores and indexes the embeddings for quick retrieval.
6. **Question Processing**: User questions are processed and matched against the stored embeddings.
7. **Answer Generation**: The AI model generates detailed answers based on the relevant text chunks.
