from show_data import *

def genre_input():
    print('\nInput list of your favourite genres to be given a list of top shows that best fit your interests\n')
    print(genre_generator())

    #takes user input and converts it into usable format
    user_genres = input('Enter genres in csv format:\n')
    user_genres.lower()
    user_genres.replace(' ', '')
    user_genres.split(',')

    if check_genres(user_genres):
        return user_genres
    else:
        genre_input()





#verifies that all user inputed generaed genres are in out list of genres
def check_genres(user_genres):
  # Define a list of allowed genres
  allowed_genres = []

  # Iterate over the list of user-provided genres
  for genre in user_genres:
    # Check if the genre is in the list of allowed genres
    if genre not in allowed_genres:
      # If the genre is not in the list of allowed genres, return False
      print(f'Sorry {genre} is not a valaid genre')
      return False

  # If all genres in the user-provided list are in the list of allowed genres, return True
  return True


genre_input()