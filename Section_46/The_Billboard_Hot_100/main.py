import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os


load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")


travel_time = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}

response = requests.get(
    url=f"https://www.billboard.com/charts/hot-100/{travel_time}/", headers=header
)
response.raise_for_status()

data = response.text

soup = BeautifulSoup(data, "html.parser")
songs = soup.select(
    selector=".o-chart-results-list-row-container .o-chart-results-list-row #title-of-a-story"
)
song_titles = [song.getText().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
    )
)

current_user = sp.current_user()
if not current_user:
    print("Please log in to Spotify.")
    exit()

# Create a new playlist
user_id = current_user["id"]
playlist = sp.user_playlist_create(
    user=user_id, name=f"{travel_time} Billboard 100", public=False
)

if not playlist:
    print("Failed to create a playlist.")
    exit()
playlist_id = playlist["id"]

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{travel_time[:4]}", type="track")
    if result and result.get("tracks") and result["tracks"].get("items"):
        uri = result["tracks"]["items"][0]["uri"]
        sp.playlist_add_items(playlist_id, items=[uri])
        print(f"{song} added to your playlist.")
    else:
        print(f"No results found for {song}. Skipped.")
