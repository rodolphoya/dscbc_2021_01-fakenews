# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1xhx7rghMQeKWRZZo9e58AO_PhFEpNN7H
"""
from joblib import load
import pandas as pd
import numpy as np
from functions import ProjectFunctions
import sklearn
import streamlit as st

class Predict:
    def predict(txt):
        model = load(open('/app/dscbc_2021_01-fakenews/programas/Lauro/App_Veritas/model.joblib', 'rb'))
        if len(txt) < 70:
            return st.error('Essa notícia é muito curta! Nosso algoritmo funciona melhor com notícias com 70 caracteres ou mais...')
        else:
            texto = (pd.Series(txt)).apply(ProjectFunctions.remover_acentos_e_numeros)
            predicao = ''
            if model.predict(texto) == 'VERDADEIRO':
                predicao = 'verdadeira'
            else:
                predicao = 'falsa'
            if (model.predict_proba(texto))*100 > 85:
                return st.success(f'A notícia parece ser {predicao}, com {(round(np.max(model.predict_proba(texto)), 2))*100}% de probabilidade.')
            elif (model.predict_proba(texto))*100 < 85 < 70:
                return st.information(f'A notícia parece ser {predicao}, com {(round(np.max(model.predict_proba(texto)), 2))*100}% de probabilidade.', 
                                      'Não se esqueça de checar com agências certificadas para ter certeza!')
            else:
                  return st.warning(f'A notícia parece ser {predicao}, com {(round(np.max(model.predict_proba(texto)), 2))*100}% de probabilidade.', 
                                      'É melhor procurar uma agência credenciada para checar essa informação para você, ok?')
