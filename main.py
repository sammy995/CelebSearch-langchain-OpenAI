import os

from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

import streamlit as st


# Streamlit UI
apikey = st.text_input("Enter your secret key. This key is not stored anywhere but is required to run the application...")
st.title('Celebrity Search')
st.subheader('Langchain Demo with OPEN AI API')
input_text = st.text_input("Enter a Celebrity name you want to search...")

os.environ["OPENAI_API_KEY"] = apikey

if apikey:
    #Prompt Template
    input_prompt1 = PromptTemplate(
        input_variables =['name'],
        template = "Tell me introduction of {name}"
    )

    #Interact with OpenAi
    llm = OpenAI(temperature=0.6)
    chain1 =LLMChain(llm=llm, prompt=input_prompt1, verbose=False, output_key='entity')

    input_prompt2 = PromptTemplate(
        input_variables =['entity'],
        template = "When was {entity} born. Give only day, month, year and nothing else."
    )

    chain2 =LLMChain(llm=llm, prompt=input_prompt2, verbose=False, output_key='birthdate')

    input_prompt3 = PromptTemplate(
        input_variables =['birthdate'],
        template = "Give 5 events in one sentence that happened on the day of {birthdate}"
    )
    chain3 =LLMChain(llm=llm, prompt=input_prompt3, verbose=False, output_key='major_events')

    main_chain = SequentialChain(
        chains=[chain1, chain2, chain3],
        input_variables=['name'],
        output_variables=['entity', 'birthdate', 'major_events'],
        verbose=True)

    if input_text:
        st.write(main_chain({'name':input_text}))


else:
    st.text("Provide your key")

