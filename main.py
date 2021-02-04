from bs4 import BeautifulSoup
import requests
import secrets
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


# date = input('What date do you want to travel to? Use the format YYYY-MM-DD: ')
date = '2006-06-01'
url = f'https://www.billboard.com/charts/hot-100/{date}'

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
song_titles_span = soup.find_all(name='span', class_='chart-element__information__song')

song_titles = [title.getText() for title in song_titles_span]

scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.SPOTIPY_CLIENT_ID,
                                               client_secret=secrets.SPOTIPY_CLIENT_SECRET,
                                               redirect_uri='http://example.com',
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path='token.txt'))

user_id = sp.current_user()['id']


def song_search():
    year = date[:4]
    song_uris = []
    for i in range(len(song_titles)):
        song_search_string = f'track: {song_titles[i]} year: {year}'
        result = sp.search(q=song_search_string)
        try:
            song_uri = result['tracks']['items'][0]['uri']
        except IndexError:
            print(f'{song_titles[i]} not found.')
        else:
            song_uris.append(song_uri)
    return song_uris


pprint(song_search())
