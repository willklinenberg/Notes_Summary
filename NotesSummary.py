import openai
import streamlit as st
import docx2txt

import promptlayer
#import Notes_config

promptlayer.api_key = st.secrets["promptlayer_api"]

file = st.file_uploader('Upload Notes File (.docx)', type=[ 'docx'])
# extract text
if file:
    text = docx2txt.process(file)

    # Swap out your 'import openai'
    openai = promptlayer.openai
    openai.api_key = st.secrets["openai_api"]

    # Do something fun 🚀
    summary = openai.Completion.create(
    engine="text-davinci-003", 
    prompt=str(text) + '\n Please write a brief summary based on the notes above', 
    pl_tags=["name-guessing", "pipeline-2"],
    max_tokens=500
    )

    st.write('Your notes summary: \n' + summary.choices[0].text)
