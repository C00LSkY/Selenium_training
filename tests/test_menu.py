import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.authorization import *

list_podmenu =[]
list_subheader =[]


def test_menu_elements(driver):
    auth(driver)
    list_menu = driver.find_elements_by_css_selector('span.name')
    for i in range(len(list_menu)):
        podmenu = driver.find_element_by_css_selector('span.name')
        list_podmenu = podmenu
        print(list_podmenu)
        line_menu = list_podmenu[i]
        driver.find_element_by_css_selector(line_menu).click()
        list_header = podmenu.find_element_by_css_selector('span.mame')
        for n in range(len(list_header)):
            list_subheader = list_header
            line_submenu = list_subheader[n]
            name_header = podmenu.find_element_by_css_selector(line_submenu).text
            podmenu.find_element_by_css_selector(line_submenu).click()
            page_header = driver.find_element_by_css_selector('h1').text
            assert name_header.upper == page_header.upper, 'PAGE HEADER IS NOT LIST HEADER MENU'

