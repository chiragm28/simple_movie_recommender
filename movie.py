#Simple Python Web crawler that suggests movie based on emotion

from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP

def scrapAndProcess(emotion):

    url = ""
    if(emotion == "sad"):
        url = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "disgust"):
        url = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "anger"):
        url = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "anticipation"):
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "fear"):
        url = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "enjoyment"):
        url = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "trust"):
        url = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
    elif(emotion == "surprise"):
        url = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

    movies = []

    try:
        if not url:
            return movies
        response = HTTP.get(url)
        data = response.text
        soup = SOUP(data, "lxml")
        flags = ["None", "X", "\n"]
        for movieName in soup.findAll('a', attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}):
            movieName = str(movieName.string)
            if movieName not in flags:
                movies.append(movieName)

    except Exception as e:
        print(e)

    return movies

if __name__ == '__main__':

    emotion = input("Enter the emotion: ").lower()
    movies = scrapAndProcess(emotion)
    if not movies:
        print("Please enter from one of the available emotions")
    for count, movie in enumerate(movies):
        if count == 10:
            break
        print(movie)
