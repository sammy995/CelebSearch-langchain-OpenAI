import os
import json
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import streamlit as st


def format_output(output):
    try:
        entity = output['entity']
        birthdate = output['birthdate']
        major_events = output['major_events']

        formatted_str = f"""### Celebrity Information
        - **Introduction**: {entity} \n
        - **Birthdate**: {birthdate}\n
        - **Major Events on that Day**: {major_events}
        """
        return formatted_str
    except KeyError as e:
        st.error(f"Key error: {e}")
        return None


# Streamlit UI
apikey = st.text_input(
    "Enter your secret key. This key is not stored anywhere but is required to run the application...", type="password")
st.title('Celebrity Search')
st.subheader('Langchain Demo with OPEN AI API')
input_text = st.text_input("Enter a Celebrity name you want to search...")

if apikey:
    os.environ["OPENAI_API_KEY"] = apikey

    if input_text:
        # Prompt Templates
        input_prompt1 = PromptTemplate(
            input_variables=['name'],
            template="Tell me the introduction of {name}"
        )

        input_prompt2 = PromptTemplate(
            input_variables=['entity'],
            template="When was {entity} born? Give only day, month, year and nothing else."
        )

        input_prompt3 = PromptTemplate(
            input_variables=['birthdate'],
            template="Give 5 events in one sentence that happened on the day of {birthdate}"
        )

        # Instantiate OpenAI LLM
        llm = OpenAI(temperature=0.6)
        chain1 = LLMChain(llm=llm, prompt=input_prompt1, verbose=False, output_key='entity')
        chain2 = LLMChain(llm=llm, prompt=input_prompt2, verbose=False, output_key='birthdate')
        chain3 = LLMChain(llm=llm, prompt=input_prompt3, verbose=False, output_key='major_events')

        # Create a SequentialChain to run the chains in order
        main_chain = SequentialChain(
            chains=[chain1, chain2, chain3],
            input_variables=['name'],
            output_variables=['entity', 'birthdate', 'major_events'],
            verbose=True
        )

        try:
            # Run the chain and format the output
            output = main_chain({'name': input_text})
            formatted_output = format_output(output)

            if formatted_output:
                st.markdown(formatted_output)
            else:
                st.error("Failed to format output.")
        except Exception as e:
            st.error(f"Error: {e}")

else:
    st.warning("Provide your key.")