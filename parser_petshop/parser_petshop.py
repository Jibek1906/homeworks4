import requests
from bs4 import BeautifulSoup as BS

URL = 'https://petshop.kg/'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_data(html):
    bs = BS(html, features='html.parser')
    items = bs.find_all('div', class_='product-grid-item')
    petshop_list = []
    for item in items:
        title = item.find('h3', class_='product-title').get_text()
        href = item.find('a').get('href')
        petshop_list.append(
            {
                'title': title,
                'href': href
            }
        )
    return petshop_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        petshop_list2 = []
        for page in range(1, 2):
            response = get_html('https://petshop.kg/cat/cat-toys/', params={'page': page})
            petshop_list2.extend(get_data(response.text))
        return petshop_list2
    else:
        raise Exception('Ошибка')

print(parsing())
        