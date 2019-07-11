"""
pytest -s -v test_parameters.py
The owls are not what they seem! OvO
"""

import pytest
from selenium import webdriver

import time
import math



@pytest.fixture(scope="function")
def browser():
#    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
#    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = "https://stepik.org/lesson/{}/step/1".format(url)
    browser.get(link)
    answer = math.log(int(time.time()))
    time.sleep(5)
    browser.find_element_by_class_name("textarea").send_keys(str(answer))  # ember-auto-resize ember-view")
    time.sleep(2)
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(3)
    message = browser.find_element_by_class_name("smart-hints__feedback").text # hints__component hints__component_showed ember-view")
    time.sleep(2)
    assert message == "Correct!", "Attention, aliens!"  # - {}".format(message)




