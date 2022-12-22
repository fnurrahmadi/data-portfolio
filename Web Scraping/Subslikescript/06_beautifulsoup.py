from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

start_time = time.time()

root = 'https://subslikescript.com'
web = f'{root}/movies'
result = requests.get(web)
content = result.text
soup = BeautifulSoup(content, 'lxml')

pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
start_page = 1
last_page = pages[-2].text
# last_page = 3

counter = 0
counters = []
movies = []
links = []
scripts = []

for page in range(1, int(last_page)+1):
    try:
        web = f'{root}/movies?page={page}'
        result = requests.get(web)
        print(f'Page {page} Started')
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('article', class_='main-article')
        ul = soup.find('ul', class_='scripts-list')
        movie_list = ul.find_all('a', href=True)

        for i,v in enumerate(movie_list):
            try:
                counter += 1
                print(f'Movie {counter} Started')
                counters.append(counter)
                movies.append(v.get_text())
                links.append(v['href'])
                print(f'Movie {counter} Done')
            except:
                print(f'Movie {counter} failed : {v.get_text()}')

        print(f'Page {page} Done')

    except:
        print(f'Page {page} failed : {web}')

    # for link in links:
    #     n = 0
    #     try:
    #         web = f'{root}/{link}'
    #         result = requests.get(web)
    #         content = result.text
    #         soup = BeautifulSoup(content, 'lxml')
    #         box = soup.find('article', class_='main-article')
    #         # title = box.find('h1').get_text()
    #         script = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
    #         scripts.append(script)
    #         print(f'Accessed {link}')
    #     except:
    #         print(f'Link {link} failed')
    #     n += 1

print(len(counters))
print(len(movies))
print(len(links))
# print(len(scripts))

dict_movies = {
    'movies':movies,
    'links':links,
    # 'script':scripts
    }

df_movies = pd.DataFrame.from_dict(dict_movies)

print(df_movies)
df_movies.to_csv('dataset_scripts_movies.csv', index=False, encoding='utf-8', sep=';')

total_time = time.time() - start_time
print("--- %s seconds ---" % (total_time))

with open('log.txt', 'w') as file:
    file.write("--- %s seconds ---" % (total_time))