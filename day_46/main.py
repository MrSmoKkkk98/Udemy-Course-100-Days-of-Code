from bs4 import BeautifulSoup
import requests

user_ask = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = requests.get(f"https://www.billboard.com/charts/hot-100/{user_ask}/")
billboard_web_page = url.text
soup = BeautifulSoup(billboard_web_page, "html.parser")
songs = soup.find_all("h3", "a-no-trucate")

song_name = []
for title in songs:
    text = title.getText(strip=True)
    song_name.append(text)
    
print(song_name)