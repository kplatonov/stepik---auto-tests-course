from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/redirect_accept.html")

#firstname = browser.find_element_by_css_selector("[name = 'firstname']")
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

current_window = browser.current_window_handle

time.sleep(2)
#browser.find_element_by_id
browser.find_element_by_class_name('trollface').click()

new_window = browser.window_handles[1]
print(current_window, new_window)
browser.switch_to_window(new_window)


#confirm = browser.switch_to.alert
#confirm.accept()

#element_text = element.text
#element_attribute_value = element.get_attribute('value')
 
input_value = browser.find_element_by_css_selector("[id = 'input_value']").text
answer = browser.find_element_by_css_selector("[id = 'answer']")
answer.send_keys(calc(input_value))

button = browser.find_element_by_class_name('btn')
button.click()

#browser.switch_to.window(window_name)
#new_window = browser.window_handles[1]
#first_window = browser.window_handles[0]