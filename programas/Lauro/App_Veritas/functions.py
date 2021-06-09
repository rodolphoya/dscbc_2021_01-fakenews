
# Manipulação de números
import numpy as np
#from os import path

# Limpeza
import re
import unicodedata

class ProjectFunctions:
    def remover_acentos_e_numeros(txt):
        # Função para remover acentos sem sacrificar letras, e retirar números e colocar
        # todas as palavras em letra minúscula, além de retirar caracteres especiais.
        # A função recebe os dados que você quer limpar.
        nfkd = unicodedata.normalize('NFKD', txt)
        palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
        palavraSemAcento = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)| ^rt|http.+?",
                                "", palavraSemAcento)
        palavraSemAcento = str(palavraSemAcento).lower()
        palavraSemAcento = re.sub(r"\d+", "", palavraSemAcento)
        palavraSemAcento = re.sub(r'  ', ' ', palavraSemAcento)
        palavraSemAcento = re.sub(r'compartilheversao para impressao comentarios',' ',
                                palavraSemAcento)
        return palavraSemAcento
