# from curses import keyname
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
options = Options()
options.page_load_strategy = 'eager'

# create driver
driver = webdriver.Firefox()

# get requests to website
driver.get('https://youtube.com')

# search up something in youtube
searchBox = driver.find_element(By.XPATH, '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
searchBox.send_keys('Genkai')

driver.implicitly_wait(10)

# click search
searchButton = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')
searchButton.click()

driver.implicitly_wait(10)

# click on video
video = driver.find_element(By.XPATH, '/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a')
print(video.text)
video.click()
