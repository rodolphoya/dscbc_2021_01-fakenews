import streamlit as st
#from predict import Predict

from joblib import load
import pandas as pd
import numpy as np
from functions import ProjectFunctions
import sklearn


def predict(txt):
    model = load('/app/dscbc_2021_01-fakenews/programas/Lauro/App_Veritas/model.joblib')
    if len(txt) < 70:
        print('Essa notícia é muito curta! Nosso algoritmo funciona melhor com notícias com 70 caracteres ou mais...')
    else:
        texto = (pd.Series(txt)).apply(ProjectFunctions.remover_acentos_e_numeros)
        predicao = ''
        if model.predict(texto) == 'VERDADEIRO':
            predicao = 'verdadeira'
        else:
            predicao = 'falsa'
        return (f'A notícia parece ser {predicao}, com {(round(np.max(model.predict_proba(texto)), 2))*100}% de probabilidade.')

def veritas():
    st.image("/app/dscbc_2021_01-fakenews/programas/Lauro/App_Veritas/data/imagem.png", use_column_width=True, width=[int])
#    use_column_width=False, clamp=False, width=1000
    st.header("**Detectando Fake News de COVID-19**")
    st.markdown("---")
    #st.subheader('Cole o texto aqui:')
    noticia = st.text_area('')
    if st.button("Analisar!"):
        return st.write(predict(noticia))
    #st.markdown("---")
    #return
