import requests
from bs4 import BeautifulSoup
import ytmusicapi
from dotenv import load_dotenv

BILLBOARD_TOP_100 = "https://www.billboard.com/charts/hot-100/"

top_100 =[]

load_dotenv()

billboard_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

user_date = input("What date do you want to travel to? (formatted yyyy-mm-dd)")

billboard_request = requests.get(BILLBOARD_TOP_100 + user_date, headers=billboard_headers)

billboard_soup = BeautifulSoup(billboard_request.content, "html.parser")

all_songs = billboard_soup.find_all("h3", class_="u-letter-spacing-0010")

for song in all_songs[:100]:
    songs = song.getText(strip=True)
    top_100.append(songs)




yt = ytmusicapi.YTMusic("browser.json")

playlist = yt.create_playlist(title=f"{user_date} Billboard Top 100",
                                    description=f"Playlist of the top 100 songs for the week of {user_date}",
                                    privacy_status="PRIVATE")

for song in top_100:
    try:
        search_results = yt.search(song, filter="songs", limit=1)
        yt.add_playlist_items(playlist, [search_results[0]["videoId"]])
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")
