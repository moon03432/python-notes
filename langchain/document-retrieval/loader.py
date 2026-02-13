import os
import sys

# load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv("../.env")
except ImportError:
    print("Warning: dotenv not found, skipping environment variable loading")

# load PDF
try:
    from langchain_community.document_loaders import PyPDFLoader
    loader = PyPDFLoader("docs/machinelearning-lecture01.pdf")
    pages = loader.load()
    
    # print pages
    print(len(pages))
    page = pages[0]
    print(page.page_content[0:500])
    print(page.metadata)
except ImportError as e:
    print(f"Error loading PDF: {e}")

# URLs
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://github.com/basecamp/handbook/blob/master/titles-for-programmers.md")
docs = loader.load()
print(docs[0].page_content[:500])