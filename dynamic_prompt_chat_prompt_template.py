from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model='gemini-3.6-flash'
)
prompt = ChatPromptTemplate([
    ('system','you are helpful expert'),
    ('human','{input}'),
    ('ai','{aiinput}')
])
while True:
    user_input = input('User : ')
    if user_input == 'exit':
        break
    model = model.invoke(user_input)

    prompt.invoke({'input':user_input,'aiinput': model.text})
    print(model.text)

print(prompt)

