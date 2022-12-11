from urllib.request import urlopen
from bs4 import BeautifulSoup

#scapes site and grabs every show within there own div conatiner and adds them to the list 'shows' 
def scrape():
    url_to_scape = 'https://www.imdb.com/list/ls066095353/'

    request_page = urlopen(url_to_scape)
    page_html = request_page.read()
    request_page.close()

    html_soup = BeautifulSoup(page_html, 'html.parser')

    shows = html_soup.find_all('div', class_='lister-item-content')

    return shows



#converts list 'shows' into csv containing title, genre, and rating. 
#later converted to a table externally with vscode extension
def csv_shows():
    filename = 'shows.csv'
    f = open(filename, 'w')

    headers = 'Title, Genres, Rating \n'
    f.write(headers)

    shows = scrape()

    for show in shows:
        title = show.find('a').text

        genre_csv = show.find('span', class_='genre').text
        genre_csv = genre_csv[1:-12]
        genre_list = genre_csv.split(', ')
        genre_seperated = ' | '.join(genre_list)

        rating = show.find('span', class_='ipl-rating-star__rating').text

        f.write(title + ', ' + genre_seperated + ', ' + rating + '\n')


    f.close()


#converts shows into a list conataining dictionarys in the format: {'Title': 'The Sopranos', 'Genres': ['Crime', 'Drama'], 'Rating': '9.2'}
def dictify_shows():
    list_of_shows = []

    shows = scrape()

    for show in shows:
        title = show.find('a').text

        genre_csv = show.find('span', class_='genre').text
        genre_csv = genre_csv[1:-12]
        genre_list = genre_csv.split(', ')

        rating = show.find('span', class_='ipl-rating-star__rating').text

        show_dict = {'Title': title, 'Genres': genre_list, 'Rating': rating}
        list_of_shows.append(show_dict)

    print(list_of_shows)        

dictify_shows()