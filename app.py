import os
from apiKey import apiKey

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
from langchain.prompts.chat import (
    ChatPromptTemplate, HumanMessagePromptTemplate)

os.environ['OPENAI_API_KEY'] = apiKey

# App framework
st.title('LangChain Youtube')
user_prompt = st.text_input('Enter your topic here:')

# Prompt templates
title_template = 'Write me a youtube video title about {topic}'
title_prompt = HumanMessagePromptTemplate.from_template(title_template)
title_chat_prompt = ChatPromptTemplate.from_messages([title_prompt])

script_template = 'Write me a youtube video script based on this title: {title} while leveraging this wikipedia research: {wikipedia_research}'
script_prompt = HumanMessagePromptTemplate.from_template(script_template)
script_chat_prompt = ChatPromptTemplate.from_messages([script_prompt])

# Memory
title_memory = ConversationBufferMemory(
    input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(
    input_key='title', memory_key='chat_history')

# Llms
chat = ChatOpenAI(temperature=0.9, model='gpt-3.5-turbo-0613', client='')

title_chain = LLMChain(llm=chat, prompt=title_chat_prompt,
                       output_key='title', memory=title_memory, verbose=True)
script_chain = LLMChain(llm=chat, prompt=script_chat_prompt,
                        output_key='script', memory=script_memory, verbose=True)

wiki = WikipediaAPIWrapper(wiki_client='')

if user_prompt:
    title = title_chain.run(user_prompt)
    wiki_research = wiki.run(user_prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    st.write(script)

    with st.expander('Title history'):
        st.info(title_memory.buffer)

    with st.expander('Script history'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia research'):
        st.info(wiki_research)
