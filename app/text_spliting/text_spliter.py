import logging
from pathlib import Path
from typing import List
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

DATA_FOLDER = "app/data"
logger = logging.getLogger(__name__)

def load_pdfs(data_folder: str = DATA_FOLDER) -> List[Document]:
    """
    Loads all PDF files from the data folder and
    returns a list of LangChain Document objects.
    """
    
    documents: List[Document] = []
    data_path = Path(data_folder)

    if not data_path.exists() or not data_path.is_dir():
        logger.warning("Data folder not found or not a directory: %s", data_path)
        return documents

    for file_path in data_path.iterdir():
        if not file_path.is_file() or file_path.suffix.lower() != ".pdf":
            continue

        try:
            reader = PdfReader(str(file_path))
        except Exception:
            logger.exception("Failed to read PDF: %s", file_path.name)
            continue

        chunks: List[str] = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                chunks.append(text)

        if not chunks:
            logger.info("No extractable text found in: %s", file_path.name)
            continue

        documents.append(
            Document(
                page_content="\n".join(chunks),
                metadata={"source": file_path.name}
            )
        )

    return documents

def split_documents(
    documents: List[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[Document]:
    """
    Splits documents into smaller chunks using
    RecursiveCharacterTextSplitter.
    """

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    split_docs = text_splitter.split_documents(documents)
    return split_docs


def load_and_split_documents(
    data_folder: str = DATA_FOLDER,
    chunk_size: int = 1000,
    chunk_overlap: int = 200
) -> List[Document]:
    """
    Convenience function that loads PDFs
    and returns split text chunks.
    """

    documents = load_pdfs(data_folder)
    split_docs = split_documents(
        documents,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return split_docs

