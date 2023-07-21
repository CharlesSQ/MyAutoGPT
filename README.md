# LangChain Youtube

This is a Streamlit app called "LangChain Youtube" that generates video titles and scripts based on user input. It utilizes the LangChain library, which includes various models and utilities to generate text content. The app leverages the GPT-3.5 Turbo model from OpenAI for language generation.

## Usage

1. Install the required dependencies by running:

```
pip install requirements.txt
```

2. Obtain your OpenAI API key and place it in a file called `apiKey.py`, or you can directly set it in the `os.environ` statement in the code.

3. Run the Streamlit app using the following command:

```
streamlit run app.py
```

4. The app will open in your browser, and you will see a text input where you can enter your desired topic for the video.

5. After entering the topic, the app will generate a video title and a script based on the input.

## Code Explanation

The main components of the code are as follows:

### Libraries and API Key

- The code imports necessary libraries such as `os`, `streamlit`, and LangChain's components.

- The `apiKey` module is imported to obtain the OpenAI API key for authorization.

### App Framework

- The Streamlit app is created using `st.title()` and `st.text_input()` to get the user's topic input.

### Prompt Templates

- The code sets up prompt templates for generating the video title and script.

- The `ChatPromptTemplate` and `HumanMessagePromptTemplate` from LangChain are used to define conversational prompts.

### Memory

- Two conversation buffer memories are created to store the conversation history for the title and script generation. These memories help maintain context during the generation process.

### Language Models (LLMs)

- The code sets up a `ChatOpenAI` model with a GPT-3.5 Turbo instance for language generation.

- Two `LLMChain` instances are created, one for the title generation and another for the script generation. These chains use the respective prompt templates and memories to generate coherent content.

### Wikipedia Research

- The code uses the LangChain `WikipediaAPIWrapper` to fetch Wikipedia research based on the user's input topic.

### User Interaction and Output

- When the user enters a topic, the app runs the title and script generation chains with the provided input.

- The resulting title and script are displayed on the web page.

- The conversation history for the title and script generations is shown in expandable sections for reference.

- The fetched Wikipedia research related to the topic is also displayed in an expandable section.

## Video Reference

This code is following the instructions of this [Youtube tutorial](https://youtu.be/MlK6SIjcjE8)

## Disclaimer

Please note that this app uses the OpenAI API, and you need to have a valid API key to run it. Make sure to follow the terms of use for the OpenAI API while using this code.
