
# Manipulação de números
import numpy as np
#from os import path

# Limpeza
import re
import unicodedata

# Visualização
from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image
import seaborn as sns
from wordcloud import WordCloud, ImageColorGenerator
from yellowbrick.classifier import ClassPredictionError
from yellowbrick.text import FreqDistVisualizer, TSNEVisualizer
from yellowbrick.model_selection import LearningCurve

# Machine Learning, vetorização e métricas
import nltk
from nltk import FreqDist
import sklearn
from sklearn.calibration import calibration_curve
from sklearn import naive_bayes, pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegressionCV
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from xgboost import XGBClassifier
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

    def plot_cloud(txt, stop_w, mask):
        # Função que retorna uma wordcloud. Ela recebe os dados que você
        # quer visualizar na nuvem.
        text = " ".join(review for review in txt.noticia)
        max = len(text)
        wordcloud = WordCloud(max_font_size = 50, 
                            max_words = max, 
                            stopwords = stop_w,
                            background_color='white',
                            mask=mask).generate(text)

        plt.figure(figsize=(30, 10))
        plt.imshow(wordcloud, interpolation = "bilinear")
        plt.axis("off")
        plt.show()

    def freq_visualiser(df, stop_w):
        # Função que retorna um histograma da frequência de palavras.
        # Ela recebe os dados que você quer visualizar.
        vectorizer = CountVectorizer(stop_words=stop_w)

        docs = vectorizer.fit_transform(df.noticia)
        features = vectorizer.get_feature_names()
        plt.figure(figsize=(20, 10))
        visualizer = FreqDistVisualizer(features=features)

        visualizer.fit(docs)

        visualizer.poof()

    def model_visual(model, classes, y_train, y_test, train_df, test_df):
        # Constrói o visualizador
        visualizer = ClassPredictionError(model, 
                                        classes=classes)
        
        plt.figure(figsize=(15, 5))

        # fita os dados no visualizador e os scores
        visualizer.fit(train_df, y_train)
        visualizer.score(test_df, y_test)
        visualizer.poof()

    def show_most_informative_features(vect, clf, n=20):
        # Mostra as palavras decisivas do dataset para a classificação.
    # A função recebe a variável do vetorizador e o modelo
        feature_names = vect.get_feature_names()
        coefs_with_fns = sorted(zip(clf.coef_[0], feature_names))
        top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
        for (coef_1, fn_1), (coef_2, fn_2) in top:
            print("\t%.4f\t%-15s\t\t%.4f\t%-15s" % (coef_1, fn_1, coef_2, fn_2))
            
    def learning_curve(model, X, y):
        visualizer_tf = LearningCurve(model, cv=KFold(n_splits=10, 
                                                    shuffle=True,
                                                    random_state=123), 
                                scoring='f1_weighted', 
                                train_sizes=np.linspace(0.3, 1.0, 10), 
                                n_jobs=-1)
        visualizer_tf.fit(X, y)
        visualizer_tf.poof() 

    '''def predict_explainer_for_training(index, model_pipeline, X_test, y_test, y_train, predict, predict_probability):
        # Mostra como foi a tomada de decisão para cada notícia classificada pelo
        # modelo. A função recebe o index de uma notícia, o pipeline do modelo,
        # as predições e as probabilidades das predições.

        y_test.reset_index(drop=True, inplace=True)
        X_test.reset_index(drop=True, inplace=True)

        # Selecionando a notícia
        i = index
        txt_instance = X_test[i]

        # Comparando a categoria real com a predição
        print("Categoria:", y_test[i], 
            "--> Predição:", predict[i],
            "| Probabilidade:", round((np.max(predict_probability[i])*100), 6), "%")
        
        # Mostrando a explicação do modelo
        explainer = lime_text.LimeTextExplainer(class_names=
                    np.unique(y_train))
        explained = explainer.explain_instance(txt_instance, 
                    model_pipeline.predict_proba, num_features=10)
        explained.show_in_notebook(text=txt_instance, predict_proba=False)

    def predict_explainer_for_test(index, model_pipeline, predict, predict_probability, X, y):
        y.reset_index(drop=True, inplace=True)
        X.reset_index(drop=True, inplace=True)

        # Selecionando a notícia
        i = index
        txt_instance = X[i]

        # Comparando a categoria real com a predição
        print("Categoria:", y[i],
            "Predição:", predict[i],
            "| Probabilidade:", round((np.max(predict_probability[i])*100), 6), "%")
        
        # Mostrando a explicação do modelo
        explainer = lime_text.LimeTextExplainer(class_names=
                    np.unique(y))
        explained = explainer.explain_instance(txt_instance, 
                    model_pipeline.predict_proba, num_features=15)
        explained.show_in_notebook(text=txt_instance, predict_proba=False)'''

    def procurando_metricas(modelo, X_train, y_train, X_test, y_test):
        # Vetorizando os datasets
        train = modelo['vectorizer'].fit_transform(X_train)
        test = modelo['vectorizer'].transform(X_test)

        # Treinando e testando
        modelo['classifier'].fit(train, y_train)
        pred = modelo['classifier'].predict(test)

        # Probabilidade das predições
        pred_prob = modelo['classifier'].predict_proba(test)
        return(print(metrics.classification_report(y_test, pred, digits=3)))
