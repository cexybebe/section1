import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


class TestRegs(unittest.TestCase):
    def test_reg_1(self):
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
            self.assertEqual("Congratulations! You have successfully registered!",
                             welcome_text), 'отсоси ниче не работает'
            print('все ок вроде')
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            driver.quit()

    def test_reg_2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
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
            self.assertEqual("Congratulations! You have successfully registered!",
                             welcome_text), 'отсоси ниче не работает'
            print('все ок вроде')
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(1)
            # закрываем браузер после всех манипуляций
            driver.quit()


if __name__ == "__main__":
    unittest.main()
