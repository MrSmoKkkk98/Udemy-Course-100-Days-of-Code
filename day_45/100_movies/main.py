from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

empire_online_web_page = response.text
soup = BeautifulSoup(empire_online_web_page, "html.parser")

headers = soup.find_all(name = "h3", class_ = "title")
film_name = []
film_rate = []
for elem in headers:
    text = elem.getText()
    if text == "12: The Godfather Part II":
        num = elem.getText().split(": ")[0]
        title = elem.getText().split(": ")[1]
        film_name.append(title)
        film_rate.append(int(num))
    else:
        num = elem.getText().split(") ")[0]
        title = elem.getText().split(") ")[1]
        film_name.append(title)
        film_rate.append(int(num))
    
movie_name = film_name[::-1]
movie_rate = film_rate[::-1]

with open("day_45/100_movies/movies.txt", mode="w", encoding="utf-8") as file:
    for i in range(100):
        file.write(f"{movie_rate[i]}) {movie_name[i]}\n")
