import numpy as np

user_preferences = np.array([[5, 4, 1, 0, 3],
                             [4, 5, 1, 0, 2],
                             [1, 1, 5, 4, 0],
                             [0, 0, 4, 5, 1],
                             [3, 2, 0, 1, 5]])

def cosine_similarity(matrix):
    norm_matrix = np.linalg.norm(matrix, axis=1, keepdims=True)
    normalized_matrix = matrix / norm_matrix
    return np.dot(normalized_matrix, normalized_matrix.T)

similarity = cosine_similarity(user_preferences)

user_index = 0
similar_users = similarity[user_index].argsort()[::-1][1:]

recommendations = np.zeros(user_preferences.shape[1])

for similar_user in similar_users:
    recommendations += user_preferences[similar_user]

for idx, item in enumerate(user_preferences[user_index]):
    if item == 0 and recommendations[idx] > 0:
        print(f'Recommended item: {idx+1}') 
        print(f'Recommended item: {idx+2}')
