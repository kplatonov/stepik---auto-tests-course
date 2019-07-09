from selenium import webdriver


import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/file_input.html")

firstname = driver.find_element_by_css_selector("[name = 'firstname']")
firstname.send_keys("Konstantin")
lastname = driver.find_element_by_css_selector("[name = 'lastname']")
lastname.send_keys("Platonov")
email = driver.find_element_by_css_selector("[name = 'email']")
email.send_keys("k.platonov@corp.mail.ru")

filename = driver.find_element_by_css_selector("[name = 'file']")
filename.send_keys(file_path)

button = driver.find_element_by_class_name('btn')
button.click()
