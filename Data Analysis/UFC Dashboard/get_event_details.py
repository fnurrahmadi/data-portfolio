from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

event_link = []
fight_link = []
win_loss = []
fighter = []
fighter_link = []
opponent = []
opponent_link = []
kd = []
strike = []
tdown = []
sub = []
weight_class = []
bonus = []
method = []
sub_method = []
round = []
time = []

file = 'web_scraping_practice\\UFCstats\\events_all_ufc.csv'
df_events = pd.read_csv(file, sep=';')

for n, link in enumerate(df_events['event_link'].values):    

    web = link
    # web = 'http://www.ufcstats.com/event-details/e15d0a2519d6a0b5'
    result = requests.get(web)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')
    tbody = soup.find('tbody', class_='b-fight-details__table-body')
    tr = tbody.find_all('tr')

    for x, r in enumerate(tr):
        
        # fighter 1
        event_link.append(link)
        fight_link.append(str.strip(tr[x]['data-link'])) # fight_link
        td = r.find_all('td')
        if len(td[0].find_all('p')) < 2: # win_loss
            win_loss.append(str.strip(td[0].find('p').text))
        else:
            win_loss.append(str.strip(td[0].find_all('p')[0].text))
        fighter.append(str.strip(td[1].find_all('p')[0].text)) # fighter
        fighter_link.append(td[1].find_all('p')[0].find('a')['href']) # fighter_link
        opponent.append(str.strip(td[1].find_all('p')[1].text)) # opponent
        opponent_link.append(td[1].find_all('p')[1].find('a')['href']) # opponent_link
        kd.append(str.strip(td[2].find_all('p')[0].text)) # kd
        strike.append(str.strip(td[3].find_all('p')[0].text)) # strike
        tdown.append(str.strip(td[4].find_all('p')[0].text)) # tdown
        sub.append(str.strip(td[5].find_all('p')[0].text)) # sub
        weight_class.append(str.strip(td[6].find('p').text)) # weight_class
        if td[6].find('p').find('img'): # bonus/championship
            bonus.append(str.strip(td[6].find('p').find('img')['src']))
        else:
            bonus.append(str.strip(""))
        if len(td[7].find_all('p')) < 2:
            method.append(str.strip(td[7].find('p').text)) # method
            sub_method.append(str.strip("")) # sub_method
        else:
            method.append(str.strip(td[7].find_all('p')[0].text)) # method
            sub_method.append(str.strip(td[7].find_all('p')[1].text)) # sub_method
        round.append(str.strip(td[8].find('p').text)) # round
        time.append(str.strip(td[9].find('p').text)) # time

        # fighter 2
        event_link.append(link)
        fight_link.append(str.strip(tr[x]['data-link'])) # fight_link
        td = r.find_all('td')
        if len(td[0].find_all('p')) < 2: # win_loss
            win_loss.append("")
        else:
            win_loss.append(str.strip(td[0].find_all('p')[1].text))
        fighter.append(str.strip(td[1].find_all('p')[1].text)) # fighter
        fighter_link.append(td[1].find_all('p')[1].find('a')['href']) # fighter_link
        opponent.append(str.strip(td[1].find_all('p')[0].text)) # opponent
        opponent_link.append(td[1].find_all('p')[0].find('a')['href']) # opponent_link
        kd.append(str.strip(td[2].find_all('p')[1].text)) # kd
        strike.append(str.strip(td[3].find_all('p')[1].text)) # strike
        tdown.append(str.strip(td[4].find_all('p')[1].text)) # tdown
        sub.append(str.strip(td[5].find_all('p')[1].text)) # sub
        weight_class.append(str.strip(td[6].find('p').text)) # weight_class
        if td[6].find('p').find('img'): # bonus/championship
            bonus.append(str.strip(td[6].find('p').find('img')['src']))
        else:
            bonus.append(str.strip(""))
        if len(td[7].find_all('p')) < 2:
            method.append(str.strip(td[7].find('p').text)) # method
            sub_method.append(str.strip("")) # sub_method
        else:
            method.append(str.strip(td[7].find_all('p')[0].text)) # method
            sub_method.append(str.strip(td[7].find_all('p')[1].text)) # sub_method
        round.append(str.strip(td[8].find('p').text)) # round
        time.append(str.strip(td[9].find('p').text)) # time

    print("successful row #", n+1)
    # delay        
    sleep(5)

dict_fight = {
    'event_link':event_link,
    'fight_link':fight_link,
    'win_loss':win_loss,
    'fighter':fighter,
    'fighter_link':fighter_link,
    'opponent':opponent,
    'opponent_link':opponent_link,
    'kd':kd,
    'strike':strike,
    'tdown':tdown,
    'sub':sub,
    'weight_class':weight_class,
    'bonus':bonus,
    'method':method,
    'sub_method':sub_method,
    'round':round,
    'time':time,
}

# print(dict_fight)

df_fight = pd.DataFrame.from_dict(dict_fight)
print(df_fight)

df_fight.to_csv('web_scraping_practice\\UFCstats\\event_details_ufc.csv', index=False, encoding='utf-8', sep=';')
print("successful")