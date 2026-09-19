from langchain_core.prompts import MessagesPlaceholder,ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatGoogleGenerativeAI(  model='gemini-3.6-flash')
prompt_template = ChatPromptTemplate([
    ('system','you are an professional royal english speaking customer care agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')

])
chat_history=[]
with open('chat_history.txt') as f:
      chat_history.extend(f.readlines())
while True:
      user_input = input('you : ')
      if user_input == 'exit':
            break
      chain = prompt_template|llm
      output=  chain.invoke({'query':user_input,'chat_history':chat_history})
      print(output.text)
print(chat_history)      
