import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
# -----------------------------------------------------------------
time_travel = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
# -----------------------------------------------------------------
URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "056bf2a599e94ae99121b9d96c6ccd61"
CLIENT_SECRET = "7fbe4ba2abe74e36b5f0e6256f996789"
# -----------------------------------------------------------------
response = requests.get(f"{URL}{time_travel}")
html = response.text
soup = BeautifulSoup(html, "html.parser")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))
userid = sp.current_user()["id"]
# -------------------------------------------------------------------
all_songs = soup.select("li.o-chart-results-list__item h3.c-title")
songs_list = [song.text.strip() for song in all_songs]
# ------------------------------------------------------------------
song_uris = []
year = time_travel.split("-")[0]

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}",type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in spotify, Skipped")


playlist = sp.user_playlist_create(user=userid, name=f"{time_travel} Billboard Top 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)