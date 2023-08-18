from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up Chrome webdriver
driver = webdriver.Firefox()

# Open YouTube
driver.get("https://www.youtube.com/")

# Find the search input field and enter the search query
search_input = driver.find_element_by_name("search_query")
search_input.send_keys("cat video")
search_input.send_keys(Keys.RETURN)

# Wait for search results to load
driver.implicitly_wait(10)

# Click on the first video in the search results
first_video = driver.find_element_by_css_selector("#contents ytd-video-renderer")
first_video.click()

# Close the webdriver
driver.quit()