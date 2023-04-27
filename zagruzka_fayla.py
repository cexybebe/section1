import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


driver = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    driver.get(link)
    time.sleep(1)
    # код, который заполняет обязательные поля
    names = driver.find_elements(By.CSS_SELECTOR, "input.form-control")
    for name in names:
        name.send_keys('Penis')

    inp = driver.find_element(By.CSS_SELECTOR, "input#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'goats.txt')  # добавляем к этому пути имя файла
    inp.send_keys(file_path)

    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()
    time.sleep(5)
finally:
    driver.quit()
