import requests
from bs4 import BeautifulSoup
import os
from spotipy import client, Spotify
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ.get("Client Id")
SPOTIFY_CLIENT_SECRETE = os.environ.get("Client Secrete")
ACCESS_TOKEN= "BQBoTMtTay2g5CHRuiFG7ALqGAepPmc57i2voirRMlFX-mv3bbFuzZVIdQi1qwAfC8N9UUrbyJ6waJDIGSRVbir9XG7UkzsEiE-PJpdGS" \
              "0VyX3K7FfxssM0UzmiG5iYb476RoCxnWWyYFDTrtIDiWoGIiZlkkjxO_4MPkfxCXyRveNGNcvu_-Op5eXln2jVYMw"

year = input("Which year do you want to travel to? YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}/")

songs_data = response.text

soup = BeautifulSoup(songs_data, "html.parser")

all_songs = soup.select(".o-chart-results-list__item #title-of-a-story")

songs = []

for song in all_songs:
    text = song.getText()
    new_text = text.replace("\n", "")
    songs.append(new_text)

# spotify = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRETE,
#                        redirect_uri="http://top100.com", scope="playlist-modify-private", show_dialog=True,
#                         cache_path="token.txt")
# spotify.get_access_token()

user = Spotify(auth=ACCESS_TOKEN)
user_id = user.current_user()["id"]


songs_uri = []

for song in songs:
    try:
        uri = user.search(q=song, limit=1, type="track")["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"The song {song} doesn't exist on Spotify!")

new_playlist = user.user_playlist_create(
    user=user_id,
    name=f"{year} 100 Billboard",
    public=False)

playlist_id = new_playlist["id"]

add_tracks = user.playlist_add_items(playlist_id=playlist_id, items=songs_uri)