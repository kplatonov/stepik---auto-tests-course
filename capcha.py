from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument('headless')

#driver = webdriver.Chrome(executable_path="selenium_venv_w10/Scripts/chromedriver.exe", chrome_options=options)
driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/math.html")

input_value = driver.find_element_by_css_selector("[id = 'input_value']")
print(input_value)
