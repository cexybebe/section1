from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration1.html"
    driver.get(link)
    # Ваш код, который заполняет обязательные поля
    firstname = driver.find_element(By.CSS_SELECTOR, "form .first_block .first_class input")
    firstname.send_keys('Penis')
    lastname = driver.find_element(By.CSS_SELECTOR, "form .first_block .second_class input")
    lastname.send_keys('Penis')
    email = driver.find_element(By.CSS_SELECTOR, "form .first_block .third_class input")
    email.send_keys('penis@penis.penis')
    late_elements = driver.find_elements(By.CSS_SELECTOR, "form .second_block input")
    for element in late_elements:
        element.send_keys("pepe!(penis)")
    time.sleep(1)
    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    print('vse normalbno')
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

    # newline at the end of file
