import streamlit as st
import ollama

st.set_page_config(
    page_title="Ollama Local Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Ollama Local Chatbot")
st.markdown("Chat with your local AI models using Streamlit and Ollama.")

with st.sidebar:
    st.header("Settings")

    try:
        models_info = ollama.list()
        available_models = [model['name'] for model in models_info['models']]
    except Exception as e:
        st.error(f"Could not connect to Ollama: {e}")
        available_models = []

    if available_models:
        selected_model = st.selectbox("Select a model", available_models)
    else:
        selected_model = st.text_input("Enter model name (e.g., llama3)", value="llama3")
        st.warning("Ollama server not detected. Please ensure Ollama is running.")

    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is on your mind?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            stream = ollama.chat(
                model=selected_model,
                messages=st.session_state.messages,
                stream=True,
            )

            for chunk in stream:
                full_response += chunk['message']['content']
                response_placeholder.markdown(full_response + "▌")

            response_placeholder.markdown(full_response)

            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"An error occurred: {e}")
