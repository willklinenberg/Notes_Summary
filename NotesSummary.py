import openai
import streamlit as st

import promptlayer
promptlayer.api_key = "pl_24c0d07de627be146bd5327daa373694"

import docx2txt

path = st.text_input(label = "Specify the path to your notes")
# extract text
if path:
    text = docx2txt.process(path)


    # Swap out your 'import openai'
    openai = promptlayer.openai
    openai.api_key = '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'

    # Do something fun 🚀
    summary = openai.Completion.create(
    engine="text-davinci-003", 
    prompt=text + '\n Please write a brief summary based on the notes above', 
    pl_tags=["name-guessing", "pipeline-2"],
    max_tokens=500
    )

    st.write('Your notes summary: \n' + summary.choices[0].text)
