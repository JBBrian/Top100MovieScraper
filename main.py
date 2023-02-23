import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

source = requests.get(URL).text

soup = BeautifulSoup(source, "html.parser")

movie_grab = soup.find_all("h3", class_="title")
movie_list = []

for movie in movie_grab:
    movie_list.append(movie.text)

movie_list.reverse()

with open("movie-list.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")






# content_names = [name.get("alt") for name in movie]
#
# print(content_names)

# Write your code below this line 👇


