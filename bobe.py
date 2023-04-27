import time
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/get_attribute.html")
time.sleep(1)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему.
# Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
x_element = driver.find_element(By.CSS_SELECTOR, "img#treasure")
x = x_element.get_attribute("valuex")

y = calc(x)

# Напишем текст ответа в найденное поле
textarea = driver.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(y)
chk = driver.find_element(By.CSS_SELECTOR, '#robotCheckbox')
chk.click()
driver.find_element(By.CSS_SELECTOR, '#robotsRule').click()
time.sleep(1)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, "button")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()