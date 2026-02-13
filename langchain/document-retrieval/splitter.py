# This code explores LangChain text splitters including:
# - CharacterTextSplitter
# - RecursiveCharacterTextSplitter
# - TokenTextSplitter
# - MarkdownHeaderTextSplitter

import os
import sys

# load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv("../.env")
except ImportError:
    print("Warning: dotenv not found, skipping environment variable loading")

# text splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter

chunk_size =26
chunk_overlap = 4

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)
c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap
)

text1 = 'abcdefghijklmnopqrstuvwxyz'
print(r_splitter.split_text(text1))

text2 = 'abcdefghijklmnopqrstuvwxyzabcdefg'
print(r_splitter.split_text(text2))

text3 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
print(r_splitter.split_text(text3))
print(c_splitter.split_text(text3))

c_splitter = CharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separator = ' '
)
print(c_splitter.split_text(text3))

# recursive splitting details
some_text = """When writing documents, writers will use document structure to group content. \
This can convey to the reader, which idea's are related. For example, closely related ideas \
are in sentances. Similar ideas are in paragraphs. Paragraphs form a document. \n\n  \
Paragraphs are often delimited with a carriage return or two carriage returns. \
Carriage returns are the "backslash n" you see embedded in this string. \
Sentences have a period at the end, but also, have a space.\
and words are separated by space."""

print("Length of some_text:", len(some_text))

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=0,
    separators=["\n\n", "\n", r"(?<=\. )", " ", ""]
)
r_splitter.split_text(some_text)

print("RecursiveCharacterTextSplitter chunks:", r_splitter.split_text(some_text))

# use recursive splitter on real document
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("docs/machinelearning-lecture01.pdf")
pages = loader.load()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=150,
    length_function=len
)

docs = text_splitter.split_documents(pages)

print(len(docs))
print(len(pages))

# token text splitter
from langchain_text_splitters import TokenTextSplitter

token_splitter = TokenTextSplitter(
    chunk_size=1,
    chunk_overlap=0
)

text1 = "foo bar bazzyfoo"

print("token_splitter.split_text(text1):", token_splitter.split_text(text1))

token_splitter = TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

docs = token_splitter.split_documents(pages)

print("len(docs) by token_splitter:", len(docs))
print("docs[0] by token_splitter:", docs[0].page_content)
print("page metadata:", pages[0].metadata)

# markdown header text splitter
from langchain_text_splitters import MarkdownHeaderTextSplitter

markdown_document = """# Title\n\n \
## Chapter 1\n\n \
Hi this is Jim\n\n Hi this is Joe\n\n \
### Section \n\n \
Hi this is Lance \n\n 
## Chapter 2\n\n \
Hi this is Molly"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

md_header_splits = markdown_splitter.split_text(markdown_document)

print("markdown_header_splits:", md_header_splits)