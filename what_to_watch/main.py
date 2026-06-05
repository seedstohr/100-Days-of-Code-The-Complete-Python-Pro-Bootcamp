import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")

top_100 = []
all_movies = soup.find_all("h3", class_="title")

for movie in all_movies:
    title = movie.getText().split(" ", 1)[1]
    top_100.append(title)

top_100 = top_100[::-1]

with open("top_100.txt", "w") as file:
    for index, movie in enumerate(top_100, start=1):
        file.write(f"{index}. {movie}\n")
