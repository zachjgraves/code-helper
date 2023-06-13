import streamlit as st
import openai
import pandas as pd
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

MODEL="text-davinci-003"

st.title("GPT-3PO")
st.subheader("Your friendly CODE helper")

instructions=st.text_area("Add instructions")
### Code Input Section 
input_code=st.text_area("Input Your Code")
### Instructions Section
language=st.selectbox("Pick a language", ["Python", "R", "JavaScript"])


if st.button("Submit"):
    prompt="Fix this code or translate if the language chosen does not match the code provided. \
        Follow any instructions listed under 'Instruction:'. \
             Code: {}, Language: {}, Instruction: {}".format(input_code, language, instructions)
    response=openai.Completion.create(
        model=MODEL,
        prompt=prompt,
        max_tokens=1000,
        temperature=0.2
    )
    st.text(response.choices[0].text)

