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
        texto = (pd.Series(txt)).apply(ProjectFunctions.remover_acentos_e_numeros)
        predicao = ''
            if model.predict(texto) == 'VERDADEIRO':
                predicao = 'verdadeira'
            else:
                predicao = 'falsa'
                return ((round(np.max(model.predict_proba(texto)), 2))*100})
