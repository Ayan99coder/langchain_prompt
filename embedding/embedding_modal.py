from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2"
    ,dimension=153
)
vector = embeddings.embed_query(
    "What is the capital of Pakistan?"
)

print(str(vector))