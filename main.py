import streamlit as st
import pickle
import pandas as pd
import requests
import gdown

# Download similarity.pkl from Google Drive
url = 'https://drive.google.com/uc?id=1CBRLZyHqDaDN6ZCxOwGL-6beYS-9INVt'
output = 'similarity.pkl'
gdown.download(url, output, quiet=False)

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to fetch poster using TMDB API
def fetch_poste(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    )
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poste(movie_id))
    return recommended_movie, recommended_movie_posters

# Streamlit page configuration
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# Zoom styling for better UI
st.markdown(
    """
    <style>
    .reportview-container .main {
        transform: scale(0.80);
        transform-origin: top center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App layout and title
st.markdown("<h1 style='text-align:center;'>🎥 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Get top 5 recommendations based on your favorite movie</h4>", unsafe_allow_html=True)

# Movie selection
selected_movie_name = st.selectbox("🔍 Select a movie you like:", movies['title'].values)

# Recommendation trigger
if st.button("🎯 Recommend"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.markdown(f"<p style='text-align:center;font-weight:bold'>{names[i]}</p>", unsafe_allow_html=True)
