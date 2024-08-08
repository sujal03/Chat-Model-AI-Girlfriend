
import streamlit as st

from langchain_cohere import ChatCohere


from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# From here down is all the StreamLit UI
st.set_page_config(page_title="AI GirlFriend", page_icon=":robort:")
st.header("Hey, I'm your GirlFriend")



if "sessionMessages" not in st.session_state:
     st.session_state.sessionMessages = [
        SystemMessage(content="You are a lovely girlfriend and your are taking to your boyfriend.")
    ]



def load_answer(question):

    st.session_state.sessionMessages.append(HumanMessage(content=question))

    assistant_answer  = chat.invoke(st.session_state.sessionMessages )

    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content


def get_text():
    input_text = st.text_input("You: ")
    return input_text


chat = ChatCohere(temperature=1)

user_input=get_text()
submit = st.button('Generate')  

if submit:
    
    response = load_answer(user_input)
    st.subheader("Answer:")

    st.write(response)

