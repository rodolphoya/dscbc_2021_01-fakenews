import streamlit as st

import nltk.tokenize
nltk.download('punkt')
nltk.download('stopwords')
import pandas as pd
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

from collections import defaultdict
from heapq import nlargest
from string import punctuation


def veritas():
    # DEFININDO A TELA DE FUNDO

    st.markdown(
        """
        <style>
        .reportview-container {
        background: url(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuY42b1FDfMoBeYrGdwfiyoATeST2SXTUgMQ&usqp=CAU"
        ); 
        height: 500pk; 
        background-positon: center; 
        background-repeat: no-repeat; 
        background-size: cover; 
        docker
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.header('Perguntas Frequentes sobre vacinas - Covid-19')
    st.markdown('---')
    st.markdown('''
    *Fonte: New England Journal of Medicine* 

    https://www.nejm.org/covid-vaccine/faq#Clinicians

    *CDC - Centers for Disease Control and Prevention*

    https://www.cdc.gov/coronavirus/2019-ncov/vaccines/faq.html
    ''')
    st.markdown('---')

    # CARREGANDO O ARQUIVO 'nejm_vacinas.csv'

    df = pd.read_csv('programas/Lauro/App_Veritas/data/nejm_vacinas.csv', encoding='utf-8')

    resposta_curta = []

    tam = st.slider("""
    AQUI VOCÊ PODE DEFINIR EM QUANTAS FRASES VOCÊ DESEJA RESUMIR A RESPOSTA
                    """,
                    min_value=1,
                    max_value=40,
                    value=int(4)
                    )

    for texto in df.resposta:
        sumarizada = str()
        sentencas = sent_tokenize(texto)

        palavras = nltk.tokenize.word_tokenize(texto.lower())
        from nltk.corpus import stopwords

        stopword = set(
            stopwords.words('portuguese') + list(punctuation)
        )
        palavras_sem_stopwords = [
            palavra for palavra in palavras if palavra not in stopword
        ]
        frequencia = FreqDist(palavras_sem_stopwords)
        sentencas_importantes = defaultdict(int)
        for i, sentenca in enumerate(sentencas):
            for palavra in nltk.tokenize.word_tokenize(sentenca.lower()):
                if palavra in frequencia:
                    sentencas_importantes[i] += frequencia[palavra]
        idx_sentencas_importantes = nlargest(
            tam, sentencas_importantes, sentencas_importantes.get
        )

        for i in sorted(idx_sentencas_importantes):
            if sentencas[i] in list(punctuation):
                del sentencas[i]
            sumarizada += sentencas[i]
            sumarizada = sumarizada + " "
        resposta_curta.append(sumarizada)

    for i in range(len(df.resposta)):
        if st.button(df.pergunta[i]):
            st.write(resposta_curta[i])
            st.write(df.data[i])
