import streamlit as st

nome = st.text_input("Digite o seu nome:")
email = st.text_input("Digite o seu email:")
if st.button("Inserir"):
    st.write("Ola ",nome," seu email eh:",email)
