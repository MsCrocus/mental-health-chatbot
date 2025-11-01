"""Utilities for building the embedding pipeline used by the chatbot."""

from typing import Tuple

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def build_vectorstore(
    documents: list[Document],
    *,
    chunk_size: int = 1000,
    chunk_overlap: int = 150,
    embedding_model: str = "all-MiniLM-L6-v2",
) -> Tuple[FAISS, int]:
    """Create a FAISS vectorstore from the provided documents.

    Args:
        documents: Source documents to embed.
        chunk_size: Maximum size of the document chunks produced by the text splitter.
        chunk_overlap: Number of overlapping characters between consecutive chunks.
        embedding_model: SentenceTransformer model name used for embeddings.

    Returns:
        A tuple with the vectorstore instance and the number of document chunks generated.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    splits = text_splitter.split_documents(documents)

    embeddings = SentenceTransformerEmbeddings(model_name=embedding_model)
    vectorstore = FAISS.from_documents(documents=splits, embedding=embeddings)

    return vectorstore, len(splits)
