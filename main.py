from bs4 import BeautifulSoup
import requests

date = input('What date do you want to travel to? Use the format YYYY-MM-DD: ')
url = f'https://www.billboard.com/charts/hot-100/{date}'

response = requests.get(url)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')
song_titles = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')

song_titles_text = [title.getText() for title in song_titles]

print(song_titles_text)
