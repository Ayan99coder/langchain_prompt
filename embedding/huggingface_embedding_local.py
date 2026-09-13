from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "LangChain is a framework for LLM applications.",
    "Hugging Face provides AI models."
]

vectors = embeddings.embed_documents(documents)

print(vectors)