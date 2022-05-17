import streamlit as st
import pickle
import pandas as pd
import requests
import base64



# 96e8703c559ee5190c27dd3444de49a7
# https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_key>>&language=en-US
# https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movies_dict)
# st.text(movies.head())

def poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?'
                 'api_key=96e8703c559ee5190c27dd3444de49a7&language=en-US'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500/"+ data['poster_path']



def recommend(movie):
    #     movie = movie.replace(" ","")
    #     movie = movie.lower()
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:11]

    recommend_movies=[]
    recommend_movies_posters =[]
    for i in movie_list:
        movie_id= movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(poster(movie_id))
    return recommend_movies,recommend_movies_posters



st.markdown('Developer- Rakshit Gupta')
st.title('Movie Recommendation System')
st.text('\n')
st.text('\n')

option=selected_movie_name=st.selectbox(
    'Enter the movie name you liked',
    movies['title'].values)

"You Selected" , option

if st.button("Recommend"):
    st.text('\n')
    st.text('\n')
    st.text('\n')
    names, posters = recommend(selected_movie_name)

    st.subheader(names[0])
    st.image(posters[0],width=300)
    st.text('\n')
    st.text('\n')
    st.text('\n')
    st.subheader("Recommendations")
    col1, col2, col3 ,col4,col5 = st.columns(5)

    with col1:

        st.image(posters[1])
        st.markdown(names[1])

    with col2:

        st.image(posters[2])
        st.markdown(names[2])
    with col3:

        st.image(posters[3])
        st.markdown(names[3])
    with col4:

        st.image(posters[4])
        st.markdown(names[4])
    with col5:

        st.image(posters[5])
        st.markdown(names[5])

    st.text('\n')
    st.text('\n')
    st.text('\n')
    col6, col7, col8, col9, col10 =st.columns(5)
    with col6:

        st.image(posters[6])
        st.markdown(names[6])
    with col7:

        st.image(posters[7])
        st.markdown(names[7])
    with col8:

        st.image(posters[8])
        st.markdown(names[8])
    with col9:

        st.image(posters[9])
        st.markdown(names[9])
    with col10:

        st.image(posters[10])
        st.markdown(names[10])