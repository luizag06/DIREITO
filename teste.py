import streamlit as st

st.write("alo mundo")

nome=st.text_input("digite o seu nome:")
if nome:
  st.write(nome.upper())
