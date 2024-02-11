from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "????????????????"
REDIRECT_URL = "http://example.com"
CLIENT_SECRET = "?????????????????"

scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri=REDIRECT_URL, client_id=CLIENT_SECRET, client_secret=CLIENT_SECRET, show_dialog=True, cache_path="token.txt"))

date = input("What year you would like to travel to in YYYY-MM-DD format.")

hot100 = "https://www.billboard.com/charts/hot-100/"

hot_date = f"https://www.billboard.com/charts/hot-100/{date}"

website = requests.get(hot_date).text

soup = BeautifulSoup(website, "html.parser")

song_names = soup.find_all(class_="chart-element__information__song text--truncate color--primary")
artist_names = soup.find_all(class_="chart-element__information__artist text--truncate color--secondary")

song_list = [song.getText() for song in song_names]
artist_list = [artist.getText() for artist in artist_names]
print(song_list)
print(artist_list)

user_id = sp.current_user()["id"]
print(user_id)

#playlist = sp.user_playlist_create(user="1171382280", name=f"{date}", public=False, collaborative=False, description=f"A playlist of the top 100 Songs of {date}")
#print(playlist)
