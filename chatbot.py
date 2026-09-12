import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

print("Program started")
print("Key loaded:", bool(os.getenv("GOOGLE_API_KEY")))

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    max_output_tokens=10000,
)

result = model.invoke("Explain LangChain in simple words")

print("RAW RESULT:")
print(result.text)

