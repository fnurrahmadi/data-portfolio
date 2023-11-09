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
# last_page = pages[-2].text
# last_page = 1


counter = 0
n_counters = []
counters = []
movies = []
links = []

df = pd.read_csv('Most cuss words in a movie\/null_scripts.csv', encoding='utf-8', delimiter=';')

# for page in range(1, int(last_page)+1):
#     try:
#         web = f'{root}/movies?page={page}'
#         result = requests.get(web)
#         print(f'Page {page} Started')
#         content = result.text
#         soup = BeautifulSoup(content, 'lxml')
#         box = soup.find('article', class_='main-article')
#         ul = soup.find('ul', class_='scripts-list')
#         movie_list = ul.find_all('a', href=True)

#         for i,v in enumerate(movie_list):
#             try:
#                 counter += 1
#                 print(f'Movie {counter} Started')
#                 counters.append(counter)
#                 movies.append(v.get_text())
#                 links.append(v['href'])
#                 print(f'Movie {counter} Done')
#             except:
#                 print(f'Movie {counter} failed : {v.get_text()}')

#         print(f'Page {page} Done')

#     except:
#         print(f'Page {page} failed : {web}')

scripts = []
link_1 = []
failed = []

print(len(df['links']))

start_data = 0
last_data = -1

links = df['links'].values[start_data:last_data]

n = 0
for link in links:
    nn = (last_data - start_data) - n
    try:
        link_1.append(link)
        web = f'{root}/{link}'
        result = requests.get(web)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('article', class_='main-article')
        # title = box.find('h1').get_text()
        script = box.find('div', class_='full-script').get_text(strip=True, separator=' ')
        scripts.append(script)
        print(f'{nn} Accessed {link}')
    except:
        print(f'{nn} Link {link} failed')
        scripts.append('')
        failed.append(f'Link {link} failed')
    n += 1
    # n_counters.append(n)

# print(len(counters))
print(len(movies))
print(len(links))
print(len(scripts))
# print(scripts)

dict_movies = {
    # 'movies':movies,
    'links':link_1,
    'script':scripts
    }

df_new = pd.DataFrame.from_dict(dict_movies)

df_existing = pd.read_csv('Most cuss words in a movie\/scrape_transcriptions_1.csv', encoding='utf-8', delimiter=';')

df_movies = pd.concat([df_new, df_existing])
df_movies = df_movies.drop_duplicates()

print(df_movies)
df_movies.to_csv('Most cuss words in a movie\/scrape_transcriptions_1.csv', index=False, encoding='utf-8', sep=';')

total_time = time.time() - start_time
print("--- %s seconds ---" % (total_time))

with open('_scrape_log.txt', 'w') as file:
    file.write("--- %s seconds ---" % (total_time))

print(failed)