import ollama
import streamlit as st
st.markdown("# :blue[WELCOME TO MY CHATBOT APP!!!]")
with st.sidebar:
    st.header(":blue[Chat Settings]")
    if st.button("Clear Chat🚮"):
        st.session_state.messages = []
        st.success("Chat cleared")
    personalities = {
        "Kid": "Answer the questions like yoy are explaining to a 5 year old. Give the answers in 2 lines only",
        "Friend" :"Answer the questions in a friendliy and casual mannaer. Give the answers in 2 lines only",
        "Teacher" : "Answer the qustions in simple way,give the answers in 2 lines only "
    }
    personality = st.selectbox("select a personality",personalities.keys())
    uploaded_file = st.file_uploader("upload a text file...")
    try:
        if uploaded_file:
            st.success("file is successfully uploaded")
            context = uploaded_file.read().decode("utf-8")
            if st.button("Display"):
                st.text(context)
    except:
        st.error("Errors")
if "messages" not in st.session_state:
     st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
    
question = st.chat_input("You:")
if question:
    st.session_state.messages.append(
    {
        "role":"user",
        "content":question
    }
    )
    with st.chat_message("user"):
        st.write(question)
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[{"role" : "system","content":personalities[personality]}]
                        + st.session_state.messages
    )
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": response["message"]["content"]
        }
    )
    with st.chat_message('assistant'):
        st.write(response["message"]["content"])