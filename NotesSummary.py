import openai
import streamlit as st

import promptlayer
promptlayer.api_key = "pl_24c0d07de627be146bd5327daa373694"


text = st.file_uploader("Choose a Notes file")
# extract text
if text:


    # Swap out your 'import openai'
    openai = promptlayer.openai
    openai.api_key = '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'

    # Do something fun 🚀
    summary = openai.Completion.create(
    engine="text-davinci-003", 
    prompt=str(text) + '\n Please write a brief summary based on the notes above', 
    pl_tags=["name-guessing", "pipeline-2"],
    max_tokens=500
    )

    st.write('Your notes summary: \n' + summary.choices[0].text)
