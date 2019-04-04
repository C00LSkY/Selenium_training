import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.authorization import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time

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

countries = []
zones = []

def test_countries(driver):
    driver.get('http://litecart/admin/?app=countries&doc=countries')
    list_countries = driver.find_elements_by_css_selector('table.dataTable tr.row')
    for c in range(len(list_countries)):
        countries_one = driver.find_element_by_css_selector('table.dataTable tr.row:nth-child(' + str(int(c+2)) + ') td:nth-child(5)')

        countries_params = countries_one.get_attribute("innerText")
        countries.append(countries_params)
    assert countries == sorted(countries)
    for z in range(len(list_countries)):
        countries_zone = driver.find_element_by_css_selector('table.dataTable tr.row:nth-child(' + str(int(z+2)) + ') td:nth-child(6)')
        countries_zone_params = countries_zone.get_attribute("innerText")
        if int(countries_zone_params) != 0:
            driver.find_element_by_css_selector('table.dataTable tr.row:nth-child(' + str(int(z+2)) + ') td:nth-child(7)').click()
            list_zones = driver.find_elements_by_css_selector('table#table-zones.dataTable tr:not(.header)')
            zones = []
            for f in range(len(list_zones)):
                zone = driver.find_element_by_css_selector('table#table-zones.dataTable tr:nth-child(' + str(int(f+2)) + ') td:nth-child(3)')
                zone_params = zone.get_attribute("innerText")
                if zone_params != "":
                    zones.append(zone_params)
            assert zones == sorted(zones)
            driver.get('http://litecart/admin/?app=countries&doc=countries')

def test_geozone(driver):
    driver.get('http://litecart/admin/?app=geo_zones&doc=geo_zones')
    list_countries_geozones = driver.find_elements_by_css_selector('table.dataTable tr.row')
    for g in range(1, len(list_countries_geozones)):
        driver.find_element_by_css_selector('table.dataTable tr.row:nth-child(' + str(int(g+1)) + ') td:nth-child(5)').click()
        list_geozone = driver.find_elements_by_css_selector('table.dataTable tr:not(.header)')
        geo = []
        for gz in range(1, len(list_geozone)):
            geozone = driver.find_element_by_css_selector("table.dataTable tr:not(.header):nth-child(" + str(int(gz+1)) + ") td:nth-child(3) [selected ='selected']")
            geozone_params = geozone.get_attribute("innerText")
            if geozone_params != "":
                geo.append(geozone_params)
        assert geo == sorted(geo)
    driver.get('http://litecart/admin/?app=geo_zones&doc=geo_zones')


def test_created_new_product(driver):
    auth_admin(driver)
    driver.get('http://litecart/admin/?app=catalog&doc=catalog')
    driver.find_element_by_css_selector('a.button[href="http://litecart/admin/?category_id=0&app=catalog&doc=edit_product"]').click()
    driver.find_element_by_css_selector('input[name="name[en]"]').send_keys("smal cat")
    driver.find_element_by_css_selector('input[name="code"]').send_keys("555555")
    driver.find_element_by_css_selector('input[value="1-3"]').click()
    driver.find_element_by_css_selector('input[name="quantity"]').send_keys("100")
    path_image = str(os.getcwd() + "\\test_data\\smal_cat.jpg")
    driver.find_element_by_css_selector('input[name="new_images[]"]').send_keys(path_image)
    driver.find_element_by_css_selector('a[href="#tab-information"]').click()
    time.sleep(1)
    driver.find_element_by_css_selector('select[name="manufacturer_id"] > option[value="1"]').click()
    driver.find_element_by_css_selector('input[name="keywords"]').send_keys("cat")
    driver.find_element_by_css_selector('input[name="short_description[en]"]').send_keys("super cat")
    driver.find_element_by_css_selector('div[class="trumbowyg-editor"]').send_keys("super cat, great toy")
    driver.find_element_by_css_selector('a[href="#tab-prices"]').click()
    time.sleep(1)
    driver.find_element_by_css_selector('input[name="purchase_price"]').send_keys("110")
    driver.find_element_by_css_selector('select[name="purchase_price_currency_code"] > option[value="USD"]').click()
    driver.find_element_by_css_selector('button[name="save"]').click()
    driver.get('http://litecart/admin/?app=catalog&doc=catalog')
    assert driver.find_elements_by_link_text('smal cat') != []





















