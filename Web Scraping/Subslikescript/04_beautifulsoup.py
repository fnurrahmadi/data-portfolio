from bs4 import BeautifulSoup
import requests

web = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(web)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()
script = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
print(title)
# print(script)

# with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    # file.write(script)