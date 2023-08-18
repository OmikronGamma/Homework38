# программа делает следующее:
# заходит на сайт ютуба
# сделать запрос *смешные видео про котов*
# и кликает мышкой на поиск
# затем кликает на видео
# и ставит лайк

# импорт библиотек
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
import random

# предустановка для неполной прогрузки сайтов
options = Options()
options.page_load_strategy = 'eager'

# выбираем браузер
# driver = webdriver.Firefox(options=options)
driver = webdriver.Chrome(options=options)

# посещаем сайт
driver.get('https://www.youtube.com/')
# driver.get('https://www.google.com/')
# driver.get('https://rutube.ru/')
sleep(1)
print('visited site')

# ищем поиск
# search_field = driver.find_element(By.ID, 'search')
# search_field = driver.find_element(By.XPATH, '//*[@id="search"]')
search_field = driver.find_element(By.CLASS_NAME, 'ytd-searchbox-spt')
# search_field = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a')      # ссылка на шортс
print('search field found')

# активируем поисковую строку
search_field.click()
print('search field activated')
sleep(1)

# находим непосредственно поиск, вводим что хотим найти, отправляем
actual_search = driver.find_element(By.CSS_SELECTOR, '.gsfi')
actual_search.send_keys('смешные видео про котов')
print('search input')
sleep(1)
search_field.submit()
print('search clicked')
sleep(2)

# Различный дебаг
# print(search_field.is_enabled())
# print(search_field.is_selected())
# print(search_field.is_displayed())

# КНОПКА поиска (иконка лупы)
# search_button = driver.find_element(By.ID, 'search-icon-legacy')
# search_button.click()
# print('search_button clicked')

# список видео из поиска
found_videos = driver.find_elements(By.CLASS_NAME, 'metadata-snippet-container')
print(len(found_videos))


# первая ссылка в найденных видео
# first_link = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string')
# first_link = driver.find_element(By.ID, 'video-title')
# first_link = driver.find_element(By.TAG_NAME, 'ytd-thumbnail')
# first_link = driver.find_element(By.CLASS_NAME, 'metadata-snippet-container')
# first_link = driver.find_element(By.CSS_SELECTOR, 'ytd-video-renderer.ytd-item-section-renderer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h3:nth-child(1) > a:nth-child(2)')
# sleep(2)
# first_link.click()
# sleep(2)


# Случайное видео
random_video = random.choice(found_videos)
random_video.click()
sleep(3)


# название ролика
video_title = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1')
print(video_title.text)

# Кнопка лайка
like_button = driver.find_element(By.ID, 'segmented-like-button')
sleep(2)
like_button.click()
print('Like button pressed')

sleep(300)
driver.close()
