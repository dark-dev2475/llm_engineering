import streamlit as st
from bot import chatbot
from langchain_core.messages import HumanMessage
import uuid  # Used to create unique IDs for each chat session

# Cache the workflow so it doesn't reload on every interaction
@st.cache_resource
def load_workflow():
    mybot = chatbot()
    workflow = mybot()
    return workflow

workflow = load_workflow()

st.title("ChatBot with Memory")

# --- Session State Management ---
# Initialize a unique thread_id for the user's session if it doesn't exist
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Chat UI ---
# Display past messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input using st.chat_input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat history and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the config with the unique thread_id for this session
    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    
    # Prepare the input message for the workflow
    input_message = {"messages": [HumanMessage(content=prompt)]}

    # Invoke the workflow with memory
    with st.spinner("Thinking..."):
        response = workflow.invoke(input_message, config=config)
        bot_response = response['messages'][-1].content

    # Add bot response to chat history and display it
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)