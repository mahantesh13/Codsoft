import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.DataFrame({
    'movieId': [1, 2, 3, 4, 5],
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E']
})

ratings = pd.DataFrame({
    'userId': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    'movieId': [1, 2, 3, 2, 3, 1, 3, 4, 2, 5, 3, 4],
    'rating': [4, 5, 3, 4, 4, 2, 5, 4, 3, 2, 5, 4]
})

user_movie_matrix = ratings.pivot_table(index='userId', columns='movieId', values='rating')

movie_similarity = cosine_similarity(user_movie_matrix.fillna(0).T)

def recommend_movies(user_id, num_recommendations=5):
    user_ratings = user_movie_matrix.loc[user_id].values
    weighted_sum = movie_similarity.dot(user_ratings)
    similarities_sum = np.array([np.abs(movie_similarity).sum(axis=1)])
    predicted_ratings = weighted_sum / similarities_sum.flatten()
    unseen_movies = np.where(np.isnan(user_ratings))[0]
    recommendations = pd.DataFrame({
        'movieId': unseen_movies + 1,
        'predicted_rating': predicted_ratings[unseen_movies]
    }).sort_values(by='predicted_rating', ascending=False)
    return movies[movies['movieId'].isin(recommendations['movieId'])]['title'].values[:num_recommendations]

user_id = 1
recommended_movies = recommend_movies(user_id)
print(f"Recommended movies for user {user_id}: {recommended_movies}")
