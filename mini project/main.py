import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie, k):
    index = movies[movies['title'] == movie].index[0]
    if k == 1:
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    elif k == 2:
        distances = sorted(list(enumerate(similarity1[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


def topmovies():
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in range(0, 10):
        movie_id = top_movies.iloc[i].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(top_movies.iloc[i].title)

    return recommended_movie_names, recommended_movie_posters


st.header('NextBinge (Movie Recommender System)')
movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
similarity1 = pickle.load(open('similarity1.pkl', 'rb'))
top_movies = pickle.load(open('top_movies.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Search or select a movie",
    movie_list
)

column1, column2, column3 = st.columns(3)
with column1:
    button1 = st.button('Show recommendations based on movie cast, director, genres')
with column2:
    button2 = st.button('Show recommendations based on movie plot')
with column3:
    button3 = st.button('Show top rated movies')
col1, col2, col3, col4, col5 = st.columns(5)
if button1:
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, 1)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
if button2:
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, 2)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
if button3:
    recommended_movie_names, recommended_movie_posters = topmovies()
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[8])
        st.image(recommended_movie_posters[8])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[9])
        st.image(recommended_movie_posters[9])
