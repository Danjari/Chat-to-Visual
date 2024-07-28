from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
from streamlit_mermaid import st_mermaid
import os
import shelve

load_dotenv()
st.title("Chat to Visual")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])


# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages
       



# Ensure openai_model is initialized in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4-turbo"


# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])
    st.markdown("""
<div style="background-color:#f0f8ff; padding:20px; border-radius:10px">
    <h2 style="color:#4b8bbe; text-align:center;">Welcome to Chat to Visual!</h2>
    <p style="font-size:18px; color:#333333;">
        Interact with a GPT-4 powered chatbot that provides well-designed and easy-to-understand diagrams.
    </p>
    <p style="font-size:18px; color:#333333;">
        Simply input your questions, and the app will generate visual diagrams to help you grasp complex concepts quickly and effectively.
    </p>
</div>
""", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Function to include instructions for generating Mermaid code
def instruct_for_mermaid(prompt):
    return f"generate the mermaid code for the following query {prompt}\n please provide only the mermaid code and nothing else, no introductory sentence, no conclusion just the code.make sure to include semi colon on every line"

# Main chat interface
if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    # Modify the prompt to include instructions
    mermaid_prompt= instruct_for_mermaid(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[{"role": "system", "content": mermaid_prompt}],
            stream=True,
        ):
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "|")
        #message_placeholder.markdown(full_response)
        # Render the Mermaid code
        # rendered_diagram = st_mermaid(full_response)
        data = full_response.replace("```", "")
        data = data.replace("mermaid", "")
        st_mermaid(data, width="100%", height="800px")
        
        

    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Save chat history after each interaction
save_chat_history(st.session_state.messages)
