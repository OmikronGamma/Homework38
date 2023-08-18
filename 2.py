# зайти на сайт https://citaty.info/
# нажать *случайная цитата
#
# нужно показать на экране в print() саму цитату

# импорт библиотек
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# создаём тхт файл
quotes_file = open('quotes.txt', 'a', encoding='UTF-8')

# заходим на сайт
driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get('https://citaty.info/')
print('visited citaty.info')
sleep(1)

# вытаскиваем 10 цитат
for i in range(10):
    random_quote_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/header/div[1]/div[3]/nav/ul/li[1]/a')     # кнопка случайной цитаты
    print('random_quote found')
    random_quote_button.click()
    print('random_quote clicked')
    quote_text = driver.find_element(By.CLASS_NAME, 'field-items')      # текст цитаты
    print(quote_text.text)
    quotes_file.write(quote_text.text)      # сохраняем текст
    quotes_file.write('\n')
    sleep(3)

quotes_file.close()
sleep(5)
driver.close()
