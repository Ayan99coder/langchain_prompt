from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"  
)

messages = [ SystemMessage(content="You are a helpful Python teacher."),
    HumanMessage(content="Explain lists in Python.")]


result = model.invoke(messages)
print(result.text)