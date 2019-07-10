import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

"""
def test_exception():
    browser.get("http://selenium1py.pythonanywhere.com/")
    with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить"):
        browser.find_element_by_css_selector("button.btn")
Если элемент будет найден, то ошибка NoSuchElementException не возникнет, и тест упадёт.

Traceback (most recent call last):
  ...
Failed: Не должно быть кнопки Отправить
"""



browser = webdriver.Chrome()

url1 = "http://suninjuly.github.io/registration1.html"
url2 = "http://suninjuly.github.io/registration2.html"

class Url:
    def __init__ (self, url):
        browser.get(url)

    def find_and_click(self):
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']").send_keys("Konstantin")
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']").send_keys("Platonov")
        browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']").send_keys("k.platonov@corp.mail.ru")
        browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control first']").send_keys("322-223")
        browser.find_element_by_xpath("//div[@class='second_block']//input[@class='form-control second']").send_keys("Moscow, Leningradsky,79k39")
        browser.find_element_by_class_name('btn').click()

    def get_answer(self):
        return(browser.find_element_by_tag_name("h1").text)

    def close(self):
        """
        // переключаемся в новое окно
        driver.switchTo().window(newWindowHandler);
        // закрываем его
        driver.close();
        // возвращаемся в предыдущее окно
        driver.switchTo().window(oldWindowHandler);
        """
        browser.quit()    #закрыть драйвер и освободить ресурсы


class TestUrl(unittest.TestCase):
    def test_url1(self):
        url = Url(url1)
        url.find_and_click()
        self.assertEqual(url.get_answer(), "Поздравляем! Вы успешно зарегистировались!", 'Error Registration 1')

    def test_url2(self):
        url = Url(url2)
        url.find_and_click()
        self.assertEqual(url.get_answer(), "Поздравляем! Вы успешно зарегистировались!", 'Error Registration 2')


if __name__ == "__main__":
    unittest.main()