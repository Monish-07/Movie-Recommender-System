import pickle
import streamlit as st
import pandas as pd

movies = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



st.title('Movie Recommender System')

option = st.selectbox("Choose the Movie You Prefer", movies['title'].values)

if st.button('Show Recommendation'):
    recommendations = recommend(option)
    st.markdown("<h3 style='text-align: center;'>Recommended Movies</h3>", unsafe_allow_html=True)
    for i in recommendations:
        st.markdown(f"<p style='text-align: center;'>{i}</p>", unsafe_allow_html=True)


# if st.button('Show Recommendation'):
#     recommendations = recommend(option)
#     for i in recommendations:
#         st.write(i)