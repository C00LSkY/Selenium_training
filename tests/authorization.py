import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import os


@pytest.fixture(scope='session', autouse=True)
def driver(request):
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    #wd = webdriver.Firefox(capabilities={"marionette": False}, firefox_binary={"c:\\Program Files (x86)\\Nightly\\firefox.exe"})
    wd = webdriver.Chrome()
    #driver.implicitly_wait(10)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://litecart/admin/login.php")
    wait = WebDriverWait(driver, 10)  # seconds
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()
    wait.until(EC.title_is("My Store"))


def auth_admin(driver):
    driver.get("http://litecart/admin/login.php")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()


def auth(driver):
    driver.get("http://litecart/en/")


