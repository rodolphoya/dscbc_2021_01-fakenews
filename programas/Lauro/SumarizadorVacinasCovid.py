from collections import defaultdict
from heapq import nlargest
from string import punctuation

import nltk.tokenize
import pandas as pd
import streamlit as st
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize

# Digite ou Cole no Terminal: streamlit run SumarizadorVacinasCovid.py
# Ir em menu => Settings => Theme: Escolha Dark
# Coloque em tela cheia com F11
# Clique ao lado do menu e selecione: Always rerun

st.markdown(
    """
    <style>
    .reportview-container {
    background: url(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuY42b1FDfMoBeYrGdwfiyoATeST2SXTUgMQ&usqp=CAU"
    ); 
    height: 500pk; 
    opacity: 0.99; 
    background-positon: center; 
    background-repeat: no-repeat; 
    background-size: cover; 
    }
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

df = pd.read_csv('nejm_vacinas.csv', encoding='utf-8')

resposta_curta = []

tam = st.slider("""
AQUI VOCÊ PODE DEFINIR EM QUANTAS FRASES VOCÊ DESEJA RESUMIR A RESPOSTA
                """,
                min_value=1,
                max_value=50,
                value=int(25)
                )

for texto in df.resposta:
    sumarizada = str()
    sentencas = sent_tokenize(texto)

    palavras = nltk.tokenize.word_tokenize(texto.lower())
    from nltk.corpus import stopwords

    stopwords = set(
        stopwords.words('portuguese') + list(punctuation)
    )
    palavras_sem_stopwords = [
        palavra for palavra in palavras if palavra not in stopwords
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
    pergunta = df.pergunta[i]
    resposta = df.resposta[i]
    resumo = resposta_curta[i]

    if st.button(pergunta):
        st.write(resumo)
        st.write(df.data[i])
