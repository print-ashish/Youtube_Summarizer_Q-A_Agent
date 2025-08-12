import streamlit as st
from agent import YoutubeAgent  # your file name here

# Create a single instance of the agent
if "agent" not in st.session_state:
    st.session_state.agent = YoutubeAgent()

# Keep the same thread ID for the session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "streamlit-thread-1"

st.title("🎥 YouTube Agent Summarizer and Q&A ")

# User input box
user_message = st.text_input("Paste the youtube video url and ask me questions ")

# If the user sends a message
if st.button("Send"):
    if user_message.strip():
        with st.spinner("Thinking..."):
            response = st.session_state.agent.run(user_message, st.session_state.thread_id)
        st.markdown(f"**Response:** {response}")

# Show thread info
st.caption(f"💾 Memory thread ID: `{st.session_state.thread_id}`")
