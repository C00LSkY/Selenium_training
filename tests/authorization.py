import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@pytest.fixture
def driver(request):
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    wd = webdriver.Firefox(capabilities={"marionette": True})
    # wd = webdriver.Chrome(capabilities={"unexpectedAlertBehaviour": "dismiss"})
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

def test_login(driver):
    driver.get("http://litecart/admin/login.php")
    wait = WebDriverWait(driver, 10) # seconds
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()
    wait.until(EC.title_is("My Store"))
