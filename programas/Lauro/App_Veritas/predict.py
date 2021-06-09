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
model = load(open('/app/dscbc_2021_01-fakenews/programas/Lauro/App_Veritas/model.joblib', 'rb'))
class Predict:
    
    def predict(txt):
        texto = (pd.Series(txt)).apply(ProjectFunctions.remover_acentos_e_numeros)
        if model.predict(texto) == 'VERDADEIRO':
            return('verdadeira')
        else:
            return('falsa')
                
    def predict_proba(txt, cs=2):
        texto = (pd.Series(txt)).apply(ProjectFunctions.remover_acentos_e_numeros)
        return ((round(np.max(model.predict_proba(texto)), cs))*100)
