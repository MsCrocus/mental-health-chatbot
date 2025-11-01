"""Helper utilities to expose retrieval capabilities for the chatbot."""

from typing import Optional

from langchain_community.vectorstores import FAISS
from langchain_core.retrievers import BaseRetriever


def build_retriever(
    vectorstore: FAISS, *, search_kwargs: Optional[dict] = None
) -> BaseRetriever:
    """Return a retriever backed by the provided FAISS vectorstore."""

    if search_kwargs:
        return vectorstore.as_retriever(search_kwargs=search_kwargs)
    return vectorstore.as_retriever()
