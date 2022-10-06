import streamlit as st
import pandas as pd

dados = pd.read_csv("dados.csv")
nome = st.text_input("Digite o seu nome:")
email = st.text_input("Digite o seu email:")
if st.button("Inserir"):
    novoReg = pd.DataFrame(list(zip(nome,email)),columns=dados.columns)
    novo = pd.concat(dados,novoReg)
    novo.to_csv("dados.csv")
    st.table(novo)
    st.write("Ola ",nome," seu email eh:",email)
