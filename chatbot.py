from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)

chat_history = [
   SystemMessage(content='you are an intelligent and have experienced to solve human problems ')
]
while True:
    user_input = input('User : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
      break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.text))
    print("AI : ",result.text)

print(chat_history)
