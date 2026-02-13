import os
import sys

# load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as e:
    print(f"Warning: dotenv not found, continuing without loading environment variables: {e}")

# 加载文档
try:
    from langchain_community.document_loaders import PyPDFLoader
except ImportError as e:
    print(f"Error loading PyPDFLoader: {e}")
    sys.exit(1)

# Load PDF
loaders = [
    # Duplicate documents on purpose - messy data
    PyPDFLoader("docs/machinelearning-lecture01.pdf"),
    PyPDFLoader("docs/machinelearning-lecture01.pdf"),
    PyPDFLoader("docs/machinelearning-lecture02.pdf"),
    PyPDFLoader("docs/machinelearning-lecture03.pdf")
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

# split documents
from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=150
)

splits = text_splitter.split_documents(docs)

print("len(splits):", len(splits))

# embedding
try:
    from langchain_huggingface import HuggingFaceEmbeddings
    
    # Use HuggingFaceEmbeddings with a default model
    # You can also specify a deepseek model if available
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
except ImportError as e:
    print(f"Error loading HuggingFaceEmbeddings: {e}")
    # Fall back to SentenceTransformerEmbeddings if HuggingFaceEmbeddings fails
    try:
        from langchain_community.embeddings import SentenceTransformerEmbeddings
        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        print("Fallback to SentenceTransformerEmbeddings successful")
    except ImportError as e2:
        print(f"Error loading SentenceTransformerEmbeddings: {e2}")
        sys.exit(1)

print("embeddings:", embeddings)

# vector store
try:
    from langchain_community.vectorstores import Chroma
except ImportError as e:
    print(f"Error loading Chroma: {e}")
    sys.exit(1)

persist_directory = 'docs/chroma/'

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory=persist_directory
)

print("number of vectordb collections:", vectorstore._collection.count())

# similarity search
question = "is there an email i can ask for help"
docs = vectorstore.similarity_search(question,k=3)
print("similarity search docs:", docs)