import sys

sys.path.append('C:/Users/rewin/Desktop/vscode/projects/Show-Recommendation-Software/show_data_formats')
from show_dict import shows



def main():
    favorite_genres = genre_input()
    sorted_shows = rank_shows(favorite_genres)
    print_top(sorted_shows)
    search_again()



def rank_shows(favorite_genres):
    # Create a dictionary to store the scores for each show
    scores = {}

    # Create a set of the user's favorite genres

    for show in shows:
        
        # Check if the show's genres intersect with the user's favorite genres
        # If there is an intersection, increment the score
        score = len(favorite_genres.intersection(show["Genres"]))
        
        show['Score'] = score
    
    # Sort the shows by their scores in descending order
    sorted_shows = sorted(shows, key=lambda x: x["Score"], reverse=True)
    
    return sorted_shows



def genre_input():
    print('\nInput list of your favourite genres to be given a list of top shows that best fit your interests\n')
    print(genre_generator())

    #takes user input and converts it into formatted set
    user_genres = input('\nEnter genres in csv format:\n')
    user_genres = user_genres.lower()
    user_genres = user_genres.title()
    user_genres = user_genres.replace(' ', '')
    user_genres = user_genres.split(',')
    user_genres = set(user_genres)

    if check_genres(user_genres):
        return user_genres
    else:
        genre_input()



#verifies that all user inputed generaed genres are in out list of genres
def check_genres(user_genres):
  # Define a list of allowed genres
  allowed_genres = genre_generator()

  # Iterate over the list of user-provided genres
  for genre in user_genres:
    # Check if the genre is in the list of allowed genres
    if genre not in allowed_genres:
      # If the genre is not in the list of allowed genres, return False
      print(f'Sorry {genre} is not a valaid genre')
      return False

  # If all genres in the user-provided list are in the list of allowed genres, return True
  return True



def genre_generator():
    genre_set = set()

    # iterate over the dictionaries in the list
    for show in shows:
        # get the list of genres from the dictionary
        genres = show['Genres']
        # add the genres to the set
        genre_set.update(genres)

    return genre_set



def print_top(sorted_shows):
    print('\n\n')
    for i in range(5):
        print('--------------------------------------------------')
        print(sorted_shows[i]['Title'] + '\n')
        print(str(sorted_shows[i]['Genres']) + '\n')
        print(sorted_shows[i]['Rating'])
    print('--------------------------------------------------')
    print('\n\n')




def search_again():
    print('Would you like to search again?')
    answer = input('y/n:  ')
    
    if answer == 'y':
        main()
    elif answer == 'n':
        return
    else:
        search_again()



main()

