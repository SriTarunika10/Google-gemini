##loading all the enviornment variables
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai 


#api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
#function to load gemini model
def get_gemini_response(question):
    response=model.generate_content(question)#passing input get output
    return response.text

#initalize streamlit app
st.set_page_config(page_title="Q&A demo")
st.header("LLM Application- GEMINI")
input=st.text_input("Input Text:",key="input")#text box
submit=st.button("Ask the question")

#when sumbit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
    