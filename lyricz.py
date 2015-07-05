import requests
from bs4 import BeautifulSoup


def get_lyrics(query):
    r = requests.get('http://search.azlyrics.com/search.php?q={}'.format(query))
    soup = BeautifulSoup(r.content)
    main_content = soup.find(class_='main-page')
    lyrics = main_content.find('a')
    r = requests.get(lyrics['href'])
    soup = BeautifulSoup(r.content)
    lyrics = soup.find(class_='ringtone')
    lyrics = lyrics.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
    lyrics = lyrics.next_element
    print lyrics.text

get_lyrics('rocket man')
