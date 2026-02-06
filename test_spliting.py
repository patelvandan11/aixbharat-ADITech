from app.text_spliting.text_spliter import load_and_split_documents

docs = load_and_split_documents()

print(f"Total chunks: {len(docs)}")
print(docs[0].page_content[:500])
print(docs[0].metadata)
