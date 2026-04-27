# 1. Import libraries
import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

import matplotlib.pyplot as plt
import seaborn as sns


# 2. Create dummy movie dataset

movies = {
    "movie": [
        "Avengers",
        "Batman",
        "Titanic",
        "Notebook",
        "Hangover",
        "Deadpool"
    ],
    "action":   [1, 1, 0, 0, 0, 1],
    "comedy":   [0, 0, 0, 0, 1, 1],
    "romance":  [0, 0, 1, 1, 0, 0],
    "thriller": [1, 1, 0, 0, 0, 1]
}

df = pd.DataFrame(movies)
print(df)
# 3. Prepare feature matrix
# Remove movie names and keep only numeric columns
features = df.drop("movie", axis=1)
# 4. Compute cosine similarity
similarity_matrix = cosine_similarity(features)



# 5. Convert similarity matrix into DataFrame
#  Rows and columns should both be movie names
similarity_df = pd.DataFrame(
    similarity_matrix,
    index=df["movie"],
    columns=df["movie"]
)

print(similarity_df)


# 6. Recommendation logic
def recommend(movie_name, top_n=2):
    # Get similarity scores for the given movie
    scores = similarity_df[movie_name]
    # Sort movies by similarity (highest first)
    scores = scores.sort_values(ascending=False)
    # Remove the movie itself
    scores = scores.drop(movie_name)
    # Return top N recommendations
    return scores.head(top_n)



a =recommend("Avengers", top_n=3)
print (a)