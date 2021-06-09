import streamlit as st
from predict import Predict
import numpy as np


def veritas():
    st.image("/app/dscbc_2021_01-fakenews/programas/Lauro/App_Veritas/data/imagem.png", use_column_width=True, width=[int])
    #    use_column_width=False, clamp=False, width=1000
    st.header("**Detectando Fake News de COVID-19**")
    st.markdown("---")
    st.markdown('''Tenha certeza que sua notícia possua mais de 70 caracteres e que trate somente de assuntos relacionados ao COVID-19, tais como medicamentos, 
             tratamentos e prevenções!
     ''')
    st.markdown("---")
    st.subheader('Cole o texto aqui:')
    noticia = st.text_area('')
    if st.button("Analisar!"):
        if len(noticia) < 70:
            return st.error('Essa notícia é muito curta! Nosso algoritmo funciona melhor com notícias com 70 caracteres ou mais...')
        else:
            predicao = Predict.predict(noticia)
            pred_proba = round(Predict.predict_proba(noticia), 2)
            
            if pred_proba > 85 and pred == 'verdadeira':
                return st.success(f'A notícia parece ser {predicao}, com {pred_proba}% de probabilidade.')
            elif if pred_proba > 85 and pred == 'falsa':
                return st.error(f'A notícia parece ser {predicao}, com {pred_proba}% de probabilidade.')
            
            elif pred_proba > 70 and pred_proba < 85:
                return st.info(f'''A notícia parece ser {predicao}, com {pred_proba}% de probabilidade. 
                                     Não se esqueça de checar com agências certificadas para ter certeza!''')
            else:
                  return st.warning(f'''A notícia parece ser {predicao}, com {pred_proba}% de probabilidade. 
                                      Recomendamos procurar uma agência credenciada para checar essa informação para você, ok?''')
