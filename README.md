## Celebrity Information Retriever
This Python application utilizes the OpenAI API and the Langchain library to retrieve information about a given celebrity. It provides an introduction, birth date, and major events that occurred on the celebrity's birth date.

### Features
User-friendly Streamlit interface for entering the celebrity name and OpenAI API key
Utilizes Langchain's PromptTemplate and LLMChain to interact with the OpenAI API
Retrieves the celebrity's introduction, birth date, and major events on their birth date
Displays the retrieved information in the Streamlit app


### Prerequisites
Python 3.x
OpenAI API key


### Installation
Clone the repository:
```
git clone https://github.com/your-username/celebrity-info-retriever.git
```

Navigate to the project directory:
```
cd celebrity-info-retriever
```

Install the required dependencies:
```
pip install -r requirements.txt
```

### Usage

Run the Streamlit app:
```
streamlit run app.py
```

Enter your OpenAI API key in the provided input field.
Enter the name of the celebrity you want to search for.
The app will display the celebrity's introduction, birth date, and major events that occurred on their birth date.


### Acknowledgments
OpenAI for providing the powerful language model API
Langchain for the easy-to-use library for building applications with large language models
Streamlit for the user-friendly interface
