import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def calc(x, y):
    return str(int(x) + int(y))


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(1)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/selects1.html")
time.sleep(1)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему.
# Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
x_element = driver.find_element(By.CSS_SELECTOR, "span#num1.nowrap")
y_element = driver.find_element(By.CSS_SELECTOR, "span#num2.nowrap")
num1 = x_element.text
num2 = y_element.text

answer = calc(num1, num2)

# Напишем текст ответа в найденное поле
select = Select(driver.find_element(By.TAG_NAME, "select"))
select.select_by_value(answer)          # ищем элемент с числом


# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(10)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()
