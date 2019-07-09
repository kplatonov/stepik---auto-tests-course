from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# любой атрибут get_attribute

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))   #EC.element_to_be_clickable((By.ID, "check"))

    
browser.find_element_by_id("book").click()

input_value = browser.find_element_by_id("input_value").text

browser.find_element_by_id("answer").send_keys(calc(input_value))


button_solve = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
button_solve.click()
