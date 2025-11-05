import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

try:
    matriz_conteudo = pd.read_csv('matriz_conteudo.csv')
except FileNotFoundError:
    st.error("Erro: Arquivo 'matriz_conteudo.csv' não encontrado. Certifique-se de que está na mesma pasta.")
    st.stop()

def combinar_caracteristicas(row):
    caracteristicas = f"{row['Gênero']} {row['Artista']} {row['Humor']} {row['Época']}"
    return caracteristicas.replace(',', '')

matriz_conteudo['tags_conteudo'] = matriz_conteudo.apply(combinar_caracteristicas, axis=1)

tfidf = TfidfVectorizer(stop_words='english')
matriz_tfidf = tfidf.fit_transform(matriz_conteudo['tags_conteudo'])


def get_recommendations_by_profile(user_preferences_string, tfidf_vectorizer, matriz_musicas, matriz_tfidf_musicas, n=3):

    vetor_usuario = tfidf_vectorizer.transform([user_preferences_string])

    similaridade_cosseno = linear_kernel(vetor_usuario, matriz_tfidf_musicas).flatten()

    indices_recomendados = similaridade_cosseno.argsort()[::-1]
    melhores_indices = indices_recomendados[:n]

    return matriz_musicas[['Nome da Música', 'Artista']].iloc[melhores_indices]



st.title("🎧 Spot.py: Sistema de Recomendação por Conteúdo")
st.markdown("---")
st.subheader("⭐ Projete seu Perfil e Receba 3 Recomendações")

opcoes_genero = ['Hip-Hop', 'Pop', 'Funk', 'Samba', 'Pagode', 'Trap', 'Alternativo', 'Rock and Roll', 'MPB', 'R&B']
opcoes_humor = ['Animado', 'Reflexivo', 'Melancólico', 'Dramático', 'Romântico', 'Confiante', 'Nostálgico', 'Intenso', 'Suave', 'Sensual', 'Triste']
opcoes_epoca = ['Anos 20', 'Anos 10', 'Anos 00', 'Anos 90', 'Anos 80', 'Anos 70', 'Anos 60']


with st.form("form_recomendacao"):
    genero = st.selectbox('Gênero Favorito:', opcoes_genero)
    humor = st.selectbox('Humor Desejado:', opcoes_humor)
    epoca = st.selectbox('Época Preferida:', opcoes_epoca)
    
    submitted = st.form_submit_button("Receber Recomendações!")

if submitted:
    user_preferences_string = f"{genero} {humor} {epoca}"
    
    recomendacoes_df = get_recommendations_by_profile(
        user_preferences_string, 
        tfidf, 
        matriz_conteudo, 
        matriz_tfidf, 
        n=3
    )

    st.markdown("### 🎶 Suas 3 Músicas Recomendadas:")
    for i, row in recomendacoes_df.iterrows():
        musica = row['Nome da Música']
        artista = row['Artista']
        st.success(f"**{i+1}. {musica}** (Artista: {artista})")