import streamlit as st

nome = st.text_input("Digite o seu nome:")
if st.button("Inserir"):
    st.write("Ola ",nome," tudo bem?")
