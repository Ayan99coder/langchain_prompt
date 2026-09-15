from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=1.2
)

user_input = st.text_input("Hi, how are you?")

if st.button("Send"):
    if user_input:
        result = model.invoke(user_input)
        st.write(result.text)
        