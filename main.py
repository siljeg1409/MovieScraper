import requests
from bs4 import BeautifulSoup
import json
from concurrent.futures import ThreadPoolExecutor
import asyncio
import time 

m_url = "https://www.imdb.com/list/ls016522954/"
score = 0
count = 0

def get_movie_list():
    print("Getting movie list...")
    response = requests.get(f"{m_url}")
    print("Filtering...")
    if response.ok:
        movies = []
        soup = BeautifulSoup(response.text, 'html.parser')
        mydivs = soup.findAll("div", {"class": "lister-item-content"})
        for div in mydivs:
            rating = div.find('span', attrs={'class': 'ipl-rating-star__rating'}).text
            movie = div.find('h3', attrs={'class': 'lister-item-header'}).find('a', href=True).text
            if(float(rating) >= score):
                movies.append([format(float(rating), '.1f'), movie])

        sMovies = sorted(movies,key=lambda x: x[0], reverse = True)
        for m in sMovies[:count]:
            print(f"Rating: {m[0]}  Movie: {m[1]}")
    
def check(value):
    if 0.50 <= float(value) <= 10:
        return False
    return True

if __name__ == '__main__':

    condition = True

    while (condition):
        score_input = input("Enter the lovest rating for a movie (1-10): ")
        condition = check(score_input) if score_input.isdigit() else True

    score = float(score_input)
    count_input = input("Enter the max movie count: ")

    while count_input.isdigit() == False:
        count_input = input("Movie count must be numeric: ")

    count = int(count_input)
    
    get_movie_list()
