import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.authorization import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

list_page_header =[]
list_name_header =[]


def test_menu_elements(driver):
    auth_admin(driver)
    list_menu = driver.find_elements_by_css_selector('li#app-')
    for i in range(len(list_menu)):
        driver.find_element_by_css_selector('li:nth-child(' + str(int(i+1)) + ')#app-').click()
        list_podmenu = driver.find_elements_by_css_selector('li#app-.selected li')
        for n in range(len(list_podmenu)):
            driver.find_element_by_css_selector('li#app-.selected li:nth-child(' + str(int(n+1)) + ')').click()
            name_header = driver.find_element_by_css_selector('li#app-.selected li:nth-child(' + str(int(n+1)) + ')').text
            page_header = driver.find_element_by_css_selector('h1').text
            if name_header != page_header:
                list_page_header.append(page_header)
                list_name_header.append(name_header)
    print("Эти названия страниц не совпадают с названием пунктов в меню: ")
    for a in range(len(list_page_header)):
        print(list_page_header[a] + " : " + list_name_header[a])


def test_sticker_presents(driver):
    auth(driver)
    # поиск всех картинок товара
    list_image = driver.find_elements_by_css_selector('.product .image')
    # количество стикеров
    sticker = driver.find_elements_by_css_selector('ul.listing-wrapper.products .sticker')
    assert int(len(sticker)) == int(len(list_image))




