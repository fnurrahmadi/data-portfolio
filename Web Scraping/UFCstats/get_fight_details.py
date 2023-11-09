from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep

event_link = []

win_loss = []
fighter = []
fighter_link = []
opponent = []
opponent_link = []
bout = []
method = []
rd_end = []
rd_time = []
rd_format = []
referee = []
details = []

rd_num = []
kd = []
sig_str = []
sig_str_pct = []
total_str = []
tdown = []
tdown_pct = []
sub_att = []
rev = []
ctrl = []

head = []
body = []
leg = []
distance = []
clinch = []
ground = []

file = 'web_scraping_practice\\UFCstats\\event_details_ufc.csv'
df = pd.read_csv(file, sep=';')

n_run = 0
for n, link in enumerate(df['event_link'].unique()):
    n_run += 1
    if n_run > 1:
        break

    # web = link
    web = 'http://www.ufcstats.com/fight-details/e3aad51099a23ba4'
    result = requests.get(web)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    # persons
    div_person = soup.find('div', class_='b-fight-details__persons clearfix')
    # details
    div_details = soup.find('div', class_='b-fight-details__fight')
    div_details_top = div_details.find('div', class_='b-fight-details__fight-head')
    div_details_bottom = div_details.find('div', class_='b-fight-details__content')
    # totals
    totals_table = soup.find_all('table', class_='b-fight-details__table js-fight-table')[0]
    # significant strikes
    sig_table = soup.find_all('table', class_='b-fight-details__table js-fight-table')[1]

    per_rd = totals_table.find_all('thead')
    totals_per_rd = totals_table.find('tbody')
    sig_per_rd = sig_table.find('tbody')

    # print(totals_per_rd)

    for i, r in enumerate(per_rd[1:0]):

        # fighter 1

        event_link.append(link)
        win_loss.append(str.strip(div_person.find_all('div', class_='b-fight-details__person')[0].find('i').get_text(strip=True)))
        fighter.append(str.strip(div_person.find_all('div', class_='b-fight-details__person')[0].find('div', class_='b-fight-details__person-text').find('h3').find('a').get_text(strip=True)))
        fighter_link.append(str.strip(div_person.find_all('div', class_='b-fight-details__person')[0].find('div', class_='b-fight-details__person-text').find('h3').find('a')['href']))
        opponent.append(str.strip(div_person.find_all('div', class_='b-fight-details__person')[1].find('div', class_='b-fight-details__person-text').find('h3').find('a').get_text(strip=True)))
        opponent_link.append(str.strip(div_person.find_all('div', class_='b-fight-details__person')[1].find('div', class_='b-fight-details__person-text').find('h3').find('a')['href']))

        bout.append(str.strip(div_details_top.find('i', class_='b-fight-details__fight-title').get_text(strip=True)))
        method.append(str.strip(div_details_bottom.find_all('p')[0].find_all('i', class_='b-fight-details__text-item_first')[0].find_all('i')[1].get_text(" ", strip=True)))
        rd_end.append(str.replace(div_details_bottom.find_all('p')[0].find_all('i', class_='b-fight-details__text-item')[0].get_text(" ", strip=True), 'Round: ', ''))
        rd_time.append(str.replace(div_details_bottom.find_all('p')[0].find_all('i', class_='b-fight-details__text-item')[1].get_text(" ", strip=True), 'Time: ', ''))
        rd_format.append(str.replace(div_details_bottom.find_all('p')[0].find_all('i', class_='b-fight-details__text-item')[2].get_text(" ", strip=True), 'Time format: ', ''))
        referee.append(str.replace(div_details_bottom.find_all('p')[0].find_all('i', class_='b-fight-details__text-item')[3].get_text(" ", strip=True), 'Referee: ', ''))
        details.append(str.replace(div_details_bottom.find_all('p')[1].get_text(" ", strip=True), 'Details: ', ''))

        rd_num.append(r.get_text(strip=True))

    for r in range(len(per_rd[1:0])):
        print(totals_per_rd[r].find('tr').find_all('td')[1].find_all('p')[0].get_text(strip=True))
        # sig_str.append(r.find('tr').find_all('td')[2].find_all('p')[0].get_text(strip=True))
        # sig_str_pct.append(r.find('tr').find_all('td')[3].find_all('p')[0].get_text(strip=True))
        # total_str.append(r.find('tr').find_all('td')[4].find_all('p')[0].get_text(strip=True))
        # tdown.append(r.find('tr').find_all('td')[5].find_all('p')[0].get_text(strip=True))
        # tdown_pct.append(r.find('tr').find_all('td')[5].find_all('p')[0].get_text(strip=True))
        # sub_att.append(r.find('tr').find_all('td')[5].find_all('p')[0].get_text(strip=True))
        # rev.append(r.find('tr').find_all('td')[5].find_all('p')[0].get_text(strip=True))

    print("successful row #", n+1)
    # delay        
    sleep(1)

# print(fighter)
# print(rd_num)
# print(total_str)

dict_fight = {
    'event_link':event_link,
    'win_loss':win_loss,
    'fighter':fighter,
    'fighter_link':fighter_link,
    'opponent':opponent,
    'opponent_link':opponent_link,
    'bout':bout,
    'method':method,
    'rd_end':rd_end,
    'rd_time':rd_time,
    'rd_format':rd_format,
    'referee':referee,
    'details':details,
    'rd_num':rd_num,
    'kd':kd,
    'sig_str':sig_str,
    'sig_str_pct':sig_str_pct,
    'total_str':total_str,
    'tdown':tdown,
    'tdown_pct':tdown_pct,
    'sub_att':sub_att,
    'rev':rev,
}

# print(dict_fight)

df_fight = pd.DataFrame.from_dict(dict_fight)
# print(df_fight)

df_fight.to_csv('web_scraping_practice\\UFCstats\\fight_details_ufc.csv', index=False, encoding='utf-8', sep=';')
print("successful")