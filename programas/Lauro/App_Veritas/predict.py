# -*- coding: utf-8 -*-
"""predict.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xhx7rghMQeKWRZZo9e58AO_PhFEpNN7H
"""
import streamlit as st
from joblib import load
import pandas as pd
import numpy as np
from functions import ProjectFunctions
import sklearn

class Predict:
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
            return st.write(f'A notícia parece ser {predicao}, com {(round(np.max(model.predict_proba(texto)), 2))*100}% de probabilidade.')
