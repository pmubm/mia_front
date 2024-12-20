import streamlit as st
import requests
from utiles import get_simple_response
from utiles import get_agent_response_API
from utiles import get_agent_response_NGROK
from utiles import get_agent_response_NGROK_et_time

st.title('Chatbot Recherche Salle de cours')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# side bar select
selection = st.sidebar.selectbox("Choisir un agent:", ["Choisir un agent","Salle de classe test","Salle de classe NGROK","Salle de classe NGROK et time"])
if selection == "Choisir un agent":
    st.title("Echo Bot")

if selection == "Salle de classe test":
    st.title("Echo Bot : Salle de classe test")
    # React to user input
    if prompt := st.chat_input("Ecrivez à l'Agent Salle de classe test"):
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


elif selection == "Salle de classe API":
    st.title("Echo Bot : Salle de classe API")
    if prompt := st.chat_input("Ecrivez à l'Agent Salle de classe API"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response, last_interactions = get_agent_response_API(prompt)
        print(f"Réponse brute de l'API : {response}") # Ligne pour le débogage

        with st.chat_message("assistant"):
            st.markdown(response)  # Affiche la réponse directement

        st.session_state.messages.append({"role": "assistant", "content": response})


elif selection == "Salle de classe NGROK":
    st.title("Echo Bot : Salle de classe NGROK")
    if prompt := st.chat_input("Ecrivez à l'Agent Salle de classe NGROK"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response, last_interactions = get_agent_response_NGROK(prompt)
        print(f"Réponse brute de l'API : {response}") # Ligne pour le débogage

        with st.chat_message("assistant"):
            st.markdown(response)  # Affiche la réponse directement

        st.session_state.messages.append({"role": "assistant", "content": response})

elif selection == "Salle de classe NGROK et time":
    st.title("Echo Bot : Salle de classe NGROK et time")
    if prompt := st.chat_input("Ecrivez à l'Agent Salle de classe NGROK"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response, elapsed_time = get_agent_response_NGROK(prompt) # Récupère la réponse ET le temps
        print(f"Réponse brute de l'API : {response}")
        print(f"Temps de requête : {elapsed_time:.2f} secondes") # Affiche le temps dans la console

        with st.chat_message("assistant"):
            st.markdown(response)
            st.markdown(f"Temps de réponse : {elapsed_time:.2f} secondes") # Affiche le temps dans le chat

        st.session_state.messages.append({"role": "assistant", "content": response})


