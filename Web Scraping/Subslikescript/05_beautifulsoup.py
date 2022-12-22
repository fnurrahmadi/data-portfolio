from bs4 import BeautifulSoup
# import time
import pandas as pd
import requests

start_page = 1
end_page = 1704

root = 'https://subslikescript.com'
web = f'{root}/movies'
# web = f'{root}/movies?page={start_page}'
result = requests.get(web)
content = result.text

soup = BeautifulSoup(content, 'lxml')

counter = 0
counters = []
movies = []
links = []
scripts = []

ul = soup.find('ul', class_='scripts-list')
movie_list = ul.find_all('a', href=True)

for i,v in enumerate(movie_list):
    counter+=1
    print(f'Page {counter} Started')
    counters.append(counter)
    movies.append(v.get_text())
    links.append(v['href'])
    print(f'Page {counter} Done')

for link in links:
    web = f'{root}/{link}'
    result = requests.get(web)
    print(f'Accessed {link}')
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find('article', class_='main-article')
    title = box.find('h1').get_text()
    script = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    scripts.append(script)
    print(f'')

dict_movies = {
    'index':counters,
    'movies':movies,
    'links':links,
    'script':scripts}

df_movies = pd.DataFrame.from_dict(dict_movies)

print(df_movies)
df_movies.to_csv('dataset_scripts1.csv', index=False, encoding='utf-8', sep=';')
