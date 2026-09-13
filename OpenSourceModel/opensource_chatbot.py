from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(repo_id = "meta-llama/Llama-3.1-8B-Instruct",task = "text-generation")
model = ChatHuggingFace(llm = llm)
data = model.invoke("hii what is the capital of pakistan and tell about its history")
print(data.content)