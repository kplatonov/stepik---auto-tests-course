from selenium import webdriver


browser = webdriver.Chrome()

url1 = "http://suninjuly.github.io/registration1.html"
url2 = "http://suninjuly.github.io/registration2.html"

browser.get(url2)

#browser.find_element_by_css_selector("[action = 'registration_result.html']")
#browser.find_element_by_class_name("first_block")
browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']").send_keys("Konstantin")
browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']").send_keys("Platonov")
browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']").send_keys("k.platonov@corp.mail.ru")

browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control first']").send_keys("322-223")
browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control second']").send_keys("Moscow, Leningradsky,79k39")

browser.find_element_by_class_name('btn').click()
