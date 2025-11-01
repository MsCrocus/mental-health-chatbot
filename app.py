"""Entry point for the mental health support assistant application."""

import os
from typing import List

import gradio as gr
import google.generativeai as genai
from langchain_community.document_loaders import HuggingFaceDatasetLoader
from langchain_core.documents import Document

from embedder import build_vectorstore
from generator import build_rag_chain, DEFAULT_SYSTEM_PROMPT
from retriever import build_retriever


DATASET_NAME = "aneerajsk/medchat_mental"
DATASET_TEXT_COLUMN = "text"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
GEMINI_MODEL = "gemini-2.0-flash"


def load_documents() -> List[Document]:
    """Load the dataset from Hugging Face into LangChain Document objects."""

    loader = HuggingFaceDatasetLoader(DATASET_NAME, page_content_column=DATASET_TEXT_COLUMN)
    return loader.load()


def init_rag_pipeline(api_key: str):
    """Construct the retriever-augmented generation pipeline."""

    documents = load_documents()
    vectorstore, total_splits = build_vectorstore(
        documents,
        embedding_model=EMBEDDING_MODEL,
    )

    retriever = build_retriever(vectorstore)

    rag_chain = build_rag_chain(
        retriever,
        model_name=GEMINI_MODEL,
        google_api_key=api_key,
        system_prompt=DEFAULT_SYSTEM_PROMPT,
    )

    return rag_chain, len(documents), total_splits


def chat_function(message, history, rag_chain):
    if not message or not message.strip():
        return "Lütfen bir soru sorun."
    try:
        return rag_chain.invoke(message)
    except Exception as exc:  # pragma: no cover - defensive logging
        return f"Bir hata oluştu: {exc}"


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY ortam değişkeni bulunamadı. Lütfen Google Gemini API anahtarınızı ayarlayın."
        )

    genai.configure(api_key=api_key)

    rag_chain, total_documents, total_splits = init_rag_pipeline(api_key)

    demo = gr.ChatInterface(
        fn=lambda message, history: chat_function(message, history, rag_chain),
        title="Zihin Sağlığı Destek Asistanı",
        description=(
            "Zihin sağlığı ile ilgili sorularınızı sorun. Bu asistan, size destek olmak için burada. "
            "Unutmayın, bu bir tıbbi tavsiye değildir."
        ),
        examples=[
            "Gelecek kaygımı nasıl yönetebilirim?",
            "Son zamanlarda hiçbir şeyden keyif almıyorum. Motivasyonumu nasıl geri kazanabilirim?",
            "Kendimi sakinleştirmek için şu anda yapabileceğim basit bir nefes egzersizi var mı?",
            "'Öz-şefkat nedir ve kendime karşı nasıl daha anlayışlı olabilirim?",
        ],
        theme="soft",
        chatbot=gr.Chatbot(height=500),
    )

    print(
        "RAG zinciri hazır! Toplam %s doküman %s parçaya bölündü." % (total_documents, total_splits)
    )
    demo.launch(share=True)


if __name__ == "__main__":
    main()
