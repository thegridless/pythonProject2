import requests
from bs4 import BeautifulSoup as BS


def parse():
    URL = 'https://www.reddit.com'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/85.0.4183.121 Safari/537.36 OPR/71.0.3770.310 '
    }

    response = requests.get(URL, headers=HEADERS)
    soup = BS(response.content, 'html.parser')
    items = soup.findAll('div', class_ = '_1oQyIsiPHYt6nx7VOmd1sz _3xuFbFM3vrCqdGuKGhhhn0 scrollerItem _3Qkp11fjcAw9I9wtLo8frE _1qftyZQ2bhqP62lbPjoGAh  Post t3_jqkc5l ')
    comps = []

    for item in items:
        comps.append({
            'title': item.find('article', class_='yn9v_hQEhjlRNZI0xspbA').get_text(strip=True)
        })
        for comp in comps:
            print(comp['title'])


parse()
