# Recommendation_System
Here is a clear and concise README for your movie recommendation system script.

# Movie Recommendation System: Content-Based Filtering

This repository features a Python implementation of a **Content-Based Recommendation System** using movie genres. It calculates the mathematical similarity between movies to suggest relevant content based on a user's selection.

## Project Overview
The script demonstrates the core mechanics of a recommendation engine. By representing movies as feature vectors (genres), it identifies which films are "closest" to one another in a multi-dimensional space.

## Technical Components
The system utilizes the following key techniques:
* **Feature Engineering**: Categorical genres (Action, Comedy, Romance, Thriller) are converted into a binary matrix.
* **Cosine Similarity**: Uses the `sklearn` library to calculate the cosine of the angle between two vectors. This determines how similar two movies are regardless of magnitude.
* **Similarity Matrix**: A structured DataFrame where every movie is compared against every other movie in the dataset.

## Dataset Structure
The system uses a dummy dataset containing:
* **Movie Titles**: The unique identifier for each film.
* **Genre Tags**: Binary indicators (0 or 1) across four distinct genres.

## Workflow
1.  **Data Creation**: A `pandas` DataFrame is built containing movie titles and their associated genres.
2.  **Matrix Preparation**: The movie titles are stripped away to create a purely numeric feature matrix.
3.  **Similarity Calculation**: `cosine_similarity` is applied to the feature matrix.
4.  **Recommendation Function**: A custom logic that sorts the similarity scores and retrieves the top $N$ most similar movies, excluding the input movie itself.

## Requirements
* Python 3.x
* pandas
* numpy
* scikit-learn
* matplotlib / seaborn (for potential visualization)

## How to Run
1.  Run the script `Recommendationsystem.py`.
2.  The output will display the raw dataset, the full similarity matrix, and a specific recommendation for "Avengers".
3.  To get recommendations for other movies, call `recommend("MovieName")` within the script.
