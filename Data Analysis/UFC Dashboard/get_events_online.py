from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

web = 'http://www.ufcstats.com/statistics/events/completed?page=all'
result = requests.get(web)
content = result.text

# result = open('FBref\\fbref_pl.html', 'r', encoding='utf8')
# content = result.read()

soup = BeautifulSoup(content, 'lxml')
table = soup.find('table', class_='b-statistics__table-events')

event_name = []
event_link = []
event_date = []
event_location = []

tbody = table.find('tbody')
tr = tbody.find_all('tr')

for x, r in enumerate(tr):
    if x <= 1:
        continue

    td = r.find_all('td')

    event_name.append(str.strip(td[0].find('i').find('a').text))
    event_link.append(td[0].find('i').find('a')['href'])
    event_date.append(str.strip(td[0].find('i').find('span').text))
    event_location.append(str.strip(td[1].text))

dict_events = {
    'event_name':event_name,
    'event_date':event_date,
    'event_link':event_link,
    'event_location':event_location,
}

df_events = pd.DataFrame.from_dict(dict_events)
print(df_events)

df_events.to_csv('web_scraping_practice\\UFCstats\\events_all_ufc.csv', index=False, encoding='utf-8', sep=';')
print("successful")