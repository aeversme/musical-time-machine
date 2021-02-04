from bs4 import BeautifulSoup
import requests
import secrets
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# date = input('What date do you want to travel to? Use the format YYYY-MM-DD: ')
date = '2006-06-01'
url = f'https://www.billboard.com/charts/hot-100/{date}'

# response = requests.get(url)
# website_html = response.text
#
# soup = BeautifulSoup(website_html, 'html.parser')
# song_titles_span = soup.find_all(name='span', class_='chart-element__information__song')
#
# song_titles = [title.getText() for title in song_titles_span]

scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secrets.SPOTIPY_CLIENT_ID,
                                               client_secret=secrets.SPOTIPY_CLIENT_SECRET,
                                               redirect_uri='http://example.com',
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path='token.txt'))

user_id = sp.current_user()['id']


# def song_search():
#     year = date[:4]
#     song_uri_list = []
#     for song in song_titles:
#         song_search_string = f'track: {song} year: {year}'
#         result = sp.search(q=song_search_string, type='track')
#         try:
#             song_uri = result['tracks']['items'][0]['uri']
#         except IndexError:
#             print(f'{song} not found on Spotify. Skipped')
#         else:
#             song_uri_list.append(song_uri)
#     return song_uri_list
#
#
# song_uris = song_search()

playlist_name = f'{date} Billboard Hot 100'

create_playlist_response = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_uri = create_playlist_response['uri']
print(playlist_uri)
