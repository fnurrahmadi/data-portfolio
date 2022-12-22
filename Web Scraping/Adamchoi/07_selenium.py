from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd

web = 'https://www.adamchoi.co.uk/overs/detailed'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(web)

all_matches_button = driver.find_element(By.XPATH, '//label[@analytics-event="All matches"]')
all_matches_button.click()

sleep(3)

season_dropdown = Select(driver.find_element(By.XPATH, '//select[@id="season"]'))
season_dropdown.select_by_visible_text('21/22')

sleep(3)

matches_table = driver.find_elements(By.XPATH, '//tr[@data-ng-repeat="match in ::dtc.$scope.matches"]')

match_date = []
home_team = []
match_score = []
away_team = []

counter = 0

print(len(matches_table))
for match in matches_table:
    counter+=1
    print(counter)
    match_date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    match_score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

dict_matches = {
    'match_date':match_date,
    'home_team':home_team,
    'match_score':match_score,
    'away_team':away_team,
}

driver.quit()


df = pd.DataFrame.from_dict(dict_matches)
df.to_csv('match_results1.csv', index=False)