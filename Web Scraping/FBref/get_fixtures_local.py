from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

# web = 'https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures'
# result = requests.get(web)
# content = result.text

result = open('FBref\\fbref_pl.html', 'r', encoding='utf8')
content = result.read()

soup = BeautifulSoup(content, 'lxml')
table = soup.find('table', class_='stats_table')

wk = []
day = []
date = []
time = []
home = []
xg_home = []
score = []
xg_away = []
away = []
attendance = []
venue = []
referee = []
match_report = []
notes = []
match_link = []

tbody = table.find('tbody')
tr = tbody.find_all('tr')

row_num = 0
for r in tr:
    if str.strip(r.find('th').get_text()) == '' or str.strip(r.find('th').get_text()) == 'Wk':
        continue
    
    l = []
    for d in r.find_all('td'):
        l.append(d)

    wk.append(r.find('th').get_text())
    day.append(l[0].get_text())
    date.append(l[1].get_text())
    time.append(l[2].get_text()[0:5])
    home.append(l[3].get_text())
    xg_home.append(l[4].get_text())
    score.append(str.replace(l[5].get_text(),'–','-'))
    xg_away.append(l[6].get_text())
    away.append(l[7].get_text())
    attendance.append(str.replace(l[8].get_text(),',',''))
    venue.append(l[9].get_text())
    referee.append(l[10].get_text())
    match_report.append(l[11].get_text())
    notes.append(l[12].get_text())
    match_link.append(r.find('td', attrs={'data-stat':'match_report'}).find('a')['href'])

    # row_num += 1
    # if row_num == 100:
    #     break

dict_matches = {
    'wk':wk,
    'day':day,
    'date':date,
    'time':time,
    'home':home,
    'xg_home':xg_home,
    'score':score,
    'xg_away':xg_away,
    'away':away,
    'attendance':attendance,
    'venue':venue,
    'referee':referee,
    'match_report':match_report,
    'notes':notes,
    'match_link':match_link
}

# print(attendance)

df_matches = pd.DataFrame.from_dict(dict_matches)
# print(df_matches)

df_matches.to_csv('FBref\\matches_england.csv', index=False, encoding='utf-8', sep=';')

# total_time = time.time() - start_time
# print("--- %s seconds ---" % (total_time))

# with open('log.txt', 'w') as file:
#     file.write("--- %s seconds ---" % (total_time))