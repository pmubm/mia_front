import streamlit as st
import requests
from utiles import get_simple_response

st.title('Chatbot Recherche Salle de cours 2')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# side bar select
selection = st.sidebar.selectbox("Choisir un agent:", ["Choisir un agent","Salle de classe"])
if selection == "Choisir un agent":
    st.title("Echo Bot")

if selection == "Salle de classe":
    st.title("Echo Bot : Salle de classe")
    # React to user input
    if prompt := st.chat_input("Ecrivez à l'Agent Salle de classe"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        #response = get_ner(client, prompt)
        response, last_interactions = get_simple_response(prompt)
        traduction_results = response

        #print(traduction_results)



        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
  
