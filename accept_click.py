from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/alert_accept.html")

#firstname = driver.find_element_by_css_selector("[name = 'firstname']")
#firstname.send_keys("Konstantin")

#alert = browser.switch_to.alert
#alert.accept()

#alert = browser.switch_to.alert
#alert_text = alert.text

#confirm = browser.switch_to.alert
#confirm.accept() or confirm.dismiss()

#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()

button = driver.find_element_by_class_name('btn')
button.click()

confirm = driver.switch_to.alert
confirm.accept()

#element_text = element.text
#element_attribute_value = element.get_attribute('value')
 
input_value = driver.find_element_by_css_selector("[id = 'input_value']").text
answer = driver.find_element_by_css_selector("[id = 'answer']")
answer.send_keys(calc(input_value))

button = driver.find_element_by_class_name('btn')
button.click()

