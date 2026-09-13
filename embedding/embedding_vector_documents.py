from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model = "gemini-embedding-2",
    dimension = 32

)
documents = [
      "LangChain is a framework for building LLM applications.",
    "Gemini is a Google AI model."
]
result = embedding.embed_documents(documents)
print(str(result))
