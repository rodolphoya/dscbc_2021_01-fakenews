import streamlit as st


def veritas():
    st.image('https://github.com/m-oxu/dscbc_2021_01-fakenews/blob/main/programas/Lauro/App_Veritas/data/imagem.png', use_column_width=True, width=[int])
#    use_column_width=False, clamp=False, width=1000
    st.header("**Detectando Fake News de COVID-19**")
    st.markdown("---")
    st.subheader('Cole o texto aqui:')
    st.text_area("🚀")
    if st.button("Analisar!"):
        print('ir para df analise carregando o texto')
    st.markdown("---")
    return
