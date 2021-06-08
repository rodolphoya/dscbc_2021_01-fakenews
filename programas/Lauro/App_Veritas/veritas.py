import streamlit as st

from multiapp import MultiApp
import fakenews
import vacinas
import cartilha
import apresentacao

# streamlit run veritas.py

st.set_page_config(page_title="Veritas", page_icon="🚀️")

padding = 0

st.markdown(f""" <style> 
.reportview-container .main .block-container{{
    padding-top: {padding}rem;
    padding-bottom: {padding}rem;
}} </style> """, unsafe_allow_html=True)

veritas = MultiApp()

veritas.add_app("Fake News", fakenews.veritas)
veritas.add_app("Perguntas Frequentes", vacinas.veritas)
veritas.add_app("Guia Prático", cartilha.veritas)
veritas.add_app("Quem somos nós", apresentacao.veritas)

veritas.run()
