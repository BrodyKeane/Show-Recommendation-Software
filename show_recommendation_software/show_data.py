import sys

sys.path.append('C:/Users/rewin/Desktop/vscode/projects/Show-Recommendation-Software/show_data_formats')
from show_dict import shows
from User_input import *

def genre_generator():
    genre_set = set()

    # iterate over the dictionaries in the list
    for show in shows:
        # get the list of genres from the dictionary
        genres = show['Genres']
        # add the genres to the set
        genre_set.update(genres)

    return genre_set

genre_generator()



def rank_shows():
    # Create a dictionary to store the scores for each show
    scores = {}

    # Create a set of the user's favorite genres
    favorite_genres = genre_input()

    # Loop through each show
    for show in shows:
    # Initialize the score for the show to 0
        score = 0
        
        # Convert the genres for the show to a set
        show_genres = set(show["Genres"])
        
        # Check if the show's genres intersect with the user's favorite genres
        # If there is an intersection, increment the score
        if favorite_genres.intersection(show_genres):
            score += 1
        
        # Add the score to the dictionary of scores
        scores[show["Title"]] = score
    
    # Sort the scores in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Print the top 3 shows
    for i in range(3):
    # Print the title of the ith highest-scoring show
    print(sorted_scores[i][0])