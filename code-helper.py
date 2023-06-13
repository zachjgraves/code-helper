import streamlit as st
import openai
#import pandas as pd
#import os

openai.api_key = os.environ["OPENAI_API_KEY"]

MODEL="text-davinci-003"

st.title("GPT-3PO")
st.subheader("Your friendly CODE helper")
### Code Input Section 
input_code=st.text_area("Input Your Code")
### Instructions Section
language=st.selectbox("Pick a language", ["Python", "R", "JavaScript", "Matlab"])
instructions=st.text_area("Add any additional instruction")

if st.button("Submit"):
    prompt="Fix this code or translate if the language chosen does not mactch the code provided. \
        Follow any instructions listed under 'Intstruction:'. \
             Code: {}, Language: {}, Instruction: {}".format(input_code, language, instructions)
    st.caption(prompt)
    response=openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        max_tokens=500,
        temperature=0
    )
    st.caption(response.choices[0].text)

