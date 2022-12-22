from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
import time
import pandas as pd

web = 'https://www.audible.com/search?node=18574784011&ref=a_search_l1_catRefs_16&pf_rd_p=daf0f1c8-2865-4989-87fb-15115ba5a6d2&pf_rd_r=FXTTNSNBBTZD47F906VK'
# web = 'https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=8a113f1a-dc38-418d-b671-3cca04245da5&pf_rd_r=43WF6Z9J07A2YZE15HEH'

options = Options()
# options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(web)
driver.maximize_window()

pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

title = []
subtitle = []
author = []
narrator = []
runtime = []
release = []
language = []
ratings = []
price = []
link = []

current_page = 1
retry = 0

# sec = 3

start_time = time.time()

while current_page <= last_page:

    # print(f'waiting {sec} seconds to load page {current_page} ...')
    # time.sleep(sec)
    # print(f'page {current_page} loaded')

    start_load = time.time()
    print('waiting for elements to load')

    try:
        container = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "adbl-impression-container")]/div/span/ul')))
        # container = driver.find_element(By.XPATH, '//div[contains(@class, "adbl-impression-container")]/div/span/ul')
        products = WebDriverWait(container, 5).until(EC.presence_of_all_elements_located((By.XPATH, './li')))
        # products = container.find_elements(By.XPATH, './li')
        print('elements loaded')
        load_time = time.time() - start_load
        print(f'load time: {load_time} secs')
    except:
        retry += 1
        print(f'load failed, retry attempt #{retry}')
        if retry < 3:
            continue
        else:
            print(f'breaking out of loop after #{retry} attempts')
            break

    len_products = len(products)
    print(f'number of items found: {len_products}')

    for product in products:
        title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        narrator.append(product.find_element(By.XPATH, './/li[contains(@class, "narratorLabel")]').text)
        runtime.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)
        release.append(product.find_element(By.XPATH, './/li[contains(@class, "releaseDateLabel")]').text)
        language.append(product.find_element(By.XPATH, './/li[contains(@class, "languageLabel")]').text)
        ratings.append(product.find_element(By.XPATH, './/li[contains(@class, "ratingsLabel")]').text)
        price.append(product.find_element(By.XPATH, './/p[contains(@id, "buybox-regular-price")]/span[2]').text)
        link.append(product.find_element(By.XPATH, './/h3/a[contains(@class, "bc-link")]').get_attribute('href'))
        try:
            subtitle.append(product.find_element(By.XPATH, './/li[contains(@class, "subtitle")]').text)
        except:
            subtitle.append("no subtitle")
            pass    
            
    print(f'page {current_page} scraped succesfully')
    current_page += 1

    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass
    
    print ('\n---\n')       


total_items = len(title)
print(f'total number of titles scraped: {total_items} titles')
time_elapsed = time.time() - start_time
print(f'total time elapsed: {time_elapsed} seconds')

driver.quit()

dict_products = {
    'title':title,
    'subtitle':subtitle,
    'narrator':narrator,
    'runtime':runtime,
    'release':release,
    'language':language,
    'ratings':ratings,
    'price':price,
    'link':link,
}

df = pd.DataFrame.from_dict(dict_products)

df.to_csv('audible_results3.csv', index=False)
print('program finished')