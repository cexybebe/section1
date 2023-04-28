import time
import unittest
from math import ceil, pow, pi, e
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/find_link_text")
time.sleep(1)


link = driver.find_element(By.LINK_TEXT, str(ceil(pow(pi, e)*10000)))
link.click()

time.sleep(1)

try:
    input1 = driver.find_element(By.TAG_NAME, 'input')
    input1.send_keys("I")
    input2 = driver.find_element(By.NAME, 'last_name')
    input2.send_keys("Love")
    input3 = driver.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Big")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Penis")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(10)

finally:
    # После выполнения всех действий мы должны не забыть закрыть окно браузера
    driver.quit()
