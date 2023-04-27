import time
from math import sin, log
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
driver.get(link)

time.sleep(1)
driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
time.sleep(1)
confirm = driver.switch_to.alert
confirm.accept()

x_element = driver.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
x = x_element.text
answer = log(abs(12 * sin(int(x))))

textarea = driver.find_element(By.CSS_SELECTOR, "#answer")
textarea.send_keys(answer)

time.sleep(1)

button = driver.find_element(By.TAG_NAME, "button")
driver.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(5)
driver.quit()