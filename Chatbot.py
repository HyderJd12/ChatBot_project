import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")
st.markdown("""
    <style>
        .centered-title {
            text-align: center;
            font-size: 26px;
        }
        .instructions {
            text-align: center;
            font-size: 16px;
            color: #999999;
        }
        .intro {
            text-align: center;
            font-size: 14px;
            color: #bbbbbb;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered-title">🤖 Simple Chatbot using Streamlit 🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="intro">Built By Farman Hyder</div>', unsafe_allow_html=True)
st.markdown('<div class="instructions">Type something and press Enter. Type <b>bye</b> to exit.</div>', unsafe_allow_html=True)
st.markdown("")

# Bot responses dictionary
responses = {
    "hello": "Hi there!",
    "hi": "Hello!",
    "hey": "Heyy 😊",
    "good morning": "Good morning! ☀️",
    "good night": "Good night! 🌙",
    "how are you": "I'm doing great, thanks!",
    "what are you doing": "I'm chatting with you!",
    "what's your name": "I'm StreamBot, your chatbot!",
    "who are you": "I'm a Python program.",
    "who is your programmer": "Farman Hyder JD is my programmer",
    "who made you": "I was created by Farman Hyder using Streamlit.",
    "who is farman hyder": "Farman is a Python developer who built me.",
    "how create you": "Farman Hyder, an intern at CodeAlpha, created me.",
    "bye": "Goodbye! Have a nice day!",
    "thanks": "You're welcome!",
    "thank you": "Glad I could help!",
    "what is python": "Python is a popular programming language.",
    "what can you do": "I can respond to simple messages!",
    "do you love me": "I'm just code, but I like chatting with you!",
    "help me": "Sure, just ask your question.",
    "i need help": "I'm here to help. Please explain more.",
    "ok": "Got it!",
    "okey": "ahhm yupp",
    "tell me something": "Fun fact: Python was named after 'Monty Python'."
}

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] #append histroy into this array

# Handle form submission
def handle_submit():
    user_message = st.session_state.user_input.strip().lower()
    if not user_message:
        return

    bot_reply = responses.get(user_message, "Sorry, I didn’t understand that.")
    st.session_state.chat_history.append(("You", user_message))
    st.session_state.chat_history.append(("Bot", bot_reply))

    # Clear input
    st.session_state.user_input = ""

    # Exit if bye
    if user_message in ["bye", "goodbye"]:
        st.balloons()
        st.snow()
        st.stop()

# --- Input form with enter key submit ---
with st.form("chat_form", clear_on_submit=False):
    user_input = st.text_input("Your Message 👇", key="user_input") 
    submitted = st.form_submit_button("Send", on_click=handle_submit)

# Show chat below
st.markdown("---")
chat = st.session_state.chat_history

# Show latest chats at the TOP (stacked upward like GPT)
for i in range(len(chat) - 2, -1, -2):  # Step -2 to get pairs
    user = chat[i]
    bot = chat[i + 1]

    if user[0] == "You":
        st.markdown(f"**🧍 You:** {user[1]}")
    if bot[0] == "Bot":
        st.markdown(f"**🤖 Bot:** {bot[1]}")
    st.markdown("")  # blank line between chats