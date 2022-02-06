import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
movie_titles = soup.findAll(name="h3", class_="title")

all_movies = []

for titles in movie_titles:
    text = titles.getText()
    all_movies.append(text)


with open("movies.txt", "w") as file:
    for number in range(len(all_movies)-1, -1, -1):
        movie = all_movies[number]
        file.write(f"{movie}\n")