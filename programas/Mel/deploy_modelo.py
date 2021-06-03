import streamlit as st

import pandas as pd
from sklearn.model_selection import train_test_split
from joblib import load


st.image('imagem.png', width=1000)
#use_column_width=False, clamp=False, width=1000

st.title("Detectando Fake News de COVID-19")
st.subheader("Está em dúvida se a notícia é verdadeira ou não?")
st.markdown("**Vamos conferir!**")

st.sidebar.image('veritas.png')
st.sidebar.header("Mais informações")

sidebar_information_1 = st.sidebar.selectbox("Fake News Covid-19", 
("Como saber o que é uma fake new", "Perguntas frequentes", "Para conhecer melhor"))
st.write(sidebar_information_1)

sidebar_information_2 = st.sidebar.selectbox("Conheça mais sobre o projeto", 
("Quem somos nós", "Contato"))
st.write(sidebar_information_2)

st.markdown("---")

texto_input = st.text_area("Cole o texto da notícia aqui:")

st.markdown("---")


#left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
#left_column.button('Analisar!')

st.button("Analisar!")


#model = load("fake_new_detection.joblib")