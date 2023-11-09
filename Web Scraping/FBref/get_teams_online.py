from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

web = 'https://fbref.com/en/comps/9/Premier-League-Stats'
result = requests.get(web)
content = result.text

# result = open('FBref\\fbref_pl_teams.html', 'r', encoding='utf8')
# content = result.read()

soup = BeautifulSoup(content, 'lxml')
table = soup.find('table', id='stats_squads_standard_for')

squad_name = []
squad_link = []
squad_id = []

tbody = table.find('tbody')
tr = tbody.find_all('tr')

row_num = 0
for r in tr:
    squad_name.append(r.find('th').get_text())
    squad_link.append(r.find('th').find('a')['href'])
    squad_id.append(str.split(r.find('th').find('a')['href'],'/')[5])

    # row_num += 1
    # if row_num == 100:
    #     break

dict_teams = {
    'squad_name':squad_name,
    'squad_link':squad_link,
    'squad_id':squad_id
}

# print(squad_id)

df_teams = pd.DataFrame.from_dict(dict_teams)
print(df_teams)

df_teams.to_csv('FBref\\teams_england.csv', index=False, encoding='utf-8', sep=';')

# total_time = time.time() - start_time
# print("--- %s seconds ---" % (total_time))

# with open('log.txt', 'w') as file:
#     file.write("--- %s seconds ---" % (total_time))