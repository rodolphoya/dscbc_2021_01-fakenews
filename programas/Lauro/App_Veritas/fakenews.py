import streamlit as st
from predict import Predict
def veritas():
    st.image("/app/dscbc_2021_01-fakenews/programas/Lauro/App_Veritas/data/imagem.png", use_column_width=True, width=[int])
#    use_column_width=False, clamp=False, width=1000
    st.header("**Detectando Fake News de COVID-19**")
    st.markdown("---")
    st.subheader('Cole o texto aqui:')
    noticia = st.text_input('')
    if st.button("Analisar!"):
        return st.write(noticia)
    #st.markdown("---")
    #return
