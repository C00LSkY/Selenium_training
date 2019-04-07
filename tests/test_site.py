import pytest
from selenium import webdriver
from tests.generators import *
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By





@pytest.fixture(scope='session', autouse=True)
def driver(request):
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    # wd = webdriver.Firefox(capabilities={"marionette": False}, firefox_binary={"c:\\Program Files (x86)\\Nightly\\firefox.exe"})
    wd = webdriver.Chrome()
    # driver.implicitly_wait(10)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

fake = Faker()
wait = WebDriverWait(driver, 10)  # seconds

def auth(driver):
    driver.get("http://litecart/en/")

# def test_sticker_presents(driver):
#     auth(driver)
#     # поиск всех картинок товара
#     list_image = driver.find_elements_by_css_selector('.product .image')
#     for k in range(len(list_image)):
#         image = driver.find_element_by_css_selector('')
#         sticker = driver.find_element_by_css_selector('ul.listing-wrapper.products .sticker')
#         assert bool(sticker) == bool(image)


def test_product_page(driver):
    auth(driver)
    list_product_home_page = driver.find_elements_by_css_selector('div#box-campaigns li.product.column.shadow.hover-light')
    for p in range(len(list_product_home_page)):
        product_hp = driver.find_element_by_css_selector('div#box-campaigns li.product.column.shadow.hover-light a.link:nth-child(' + str(int(p + 1)) + ')')
        attr_product_hp = product_hp.get_attribute("innerText")
        name_product_hp = product_hp.find_element_by_css_selector('div.name').get_attribute('innerText')
        price_hp = product_hp.find_element_by_css_selector('s.regular-price').get_attribute('innerText')
        assert product_hp.find_element_by_css_selector('s.regular-price').value_of_css_property('color') == 'rgba(119, 119, 119, 1)'
        assert product_hp.find_element_by_css_selector('s.regular-price').value_of_css_property('text-decoration-line') == 'line-through'
        price_discount_hp = product_hp.find_element_by_css_selector('strong.campaign-price').get_attribute('innerText')
        assert product_hp.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color') == 'rgba(204, 0, 0, 1)'
        assert product_hp.find_element_by_css_selector('strong.campaign-price').value_of_css_property(
            'font-weight') >= '700'
        font_size_price_hp = product_hp.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size')
        font_size_price_discount_hp = product_hp.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size')
        assert int(font_size_price_hp[0:2]) < int(font_size_price_discount_hp[0:2])
        product_hp.click()
        name_product_pp = driver.find_element_by_css_selector('h1.title').get_attribute('innerText')
        assert name_product_pp == name_product_hp in attr_product_hp
        price_pp = driver.find_element_by_css_selector('s.regular-price').get_attribute('innerText')
        assert driver.find_element_by_css_selector('s.regular-price').value_of_css_property(
            'color') == 'rgba(102, 102, 102, 1)'
        assert driver.find_element_by_css_selector('s.regular-price').value_of_css_property(
            'text-decoration-line') == 'line-through', 'REGULAR PRICE IS NOT CROSSED OUT'
        assert price_pp == price_hp in attr_product_hp, 'REGULAR PRICE HOME PAGE NOT EQUAL REGULAR PRICE PRODUCT PAGE'
        price_discount_pp = driver.find_element_by_css_selector('strong.campaign-price').get_attribute('innerText')
        assert driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property(
            'color') == 'rgba(204, 0, 0, 1)', 'COLOR DISCOUNT PRICE IS NOT RED'
        assert driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property(
            'font-weight') >= '700', 'SIZE DISCOUNT PRICE IS SMALL'
        font_size_price_pp = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size')
        font_size_price_discount_pp = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size')
        assert int(font_size_price_pp[0:2]) < int(font_size_price_discount_pp[0:2]), 'SIZE DISCOUNT PRICE LESS SIZE REGULAR PRICE'
        assert price_discount_pp == price_discount_hp in attr_product_hp, 'PRICE DISCOUNT HOME PAGE NOT EQUAL PRICE DISCOUNT PRODUCT PAGE'


def test_registration_new_user(driver):
    auth(driver)
    fio = generator_user_name()
    adress = generetor_adress()
    email = generator_email()
    driver.find_element_by_css_selector('a[href="http://litecart/en/create_account"]').click()
    driver.find_element_by_css_selector('input[name="firstname"]').send_keys(fio[1])
    driver.find_element_by_css_selector('input[name="lastname"]').send_keys(fio[0])
    driver.find_element_by_css_selector('input[name="address1"]').send_keys(adress[2:7])
    driver.find_element_by_css_selector('input[name="postcode"]').send_keys("55555")
    driver.find_element_by_css_selector('input[name="city"]').send_keys(adress[1])
    driver.find_element_by_css_selector('span.select2-selection__arrow').click()
    driver.find_element_by_css_selector('input.select2-search__field').clear()
    driver.find_element_by_css_selector('input.select2-search__field').send_keys('United States')
    driver.find_element_by_css_selector('input.select2-search__field').send_keys(Keys.ENTER)
    driver.find_element_by_css_selector('input[name="email"]').send_keys(email)
    driver.find_element_by_css_selector('input[name="phone"]').send_keys("7777777777")
    driver.find_element_by_css_selector('input[name="password"]').send_keys("user")
    driver.find_element_by_css_selector('input[name="confirmed_password"]').send_keys("user")
    driver.find_element_by_css_selector('button[name="create_account"]').click()
    driver.find_element_by_css_selector('a[href="http://litecart/en/logout"]').click()
    driver.find_element_by_css_selector('input[name="email"]').send_keys(email)
    driver.find_element_by_css_selector('input[name="password"]').send_keys("user")
    driver.find_element_by_css_selector('button[name="login"]').click()
    assert driver.find_elements_by_css_selector('a[href="http://litecart/en/logout"]') != [], 'USER NOT LOGIN'
    driver.find_element_by_css_selector('a[href="http://litecart/en/logout"]').click()


def test_add_to_cart(driver):
    auth(driver)
    count = 1
    while int(count) < 3:
        driver.find_element_by_css_selector('div.content img.image').click()
        time.sleep(2)
        if len(driver.find_elements_by_css_selector('a.main-image.fancybox.zoomable.shadow > div.sticker.sale')) > 0:
            time.sleep(2)
            driver.find_element_by_css_selector('select[name="options[Size]"] > option[value="Small"]').click()
            time.sleep(2)
            driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
            # time.sleep(2)
            wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR('a.content span.quantity'), str(count)))
            count = driver.find_element_by_css_selector('span.quantity').get_attribute('innerText')
            driver.get("http://litecart/en/")
        else:
            driver.find_element_by_css_selector('button[name="add_cart_product"]').click()
            # time.sleep(2)
            wait.until(EC.text_to_be_present_in_element(By.CSS_SELECTOR('a.content span.quantity'), str(count)))
            count = driver.find_element_by_css_selector('span.quantity').get_attribute('innerText')
            driver.get("http://litecart/en/")
    driver.find_element_by_css_selector('a.link[href="http://litecart/en/checkout"]').click()
    driver.find_element_by_css_selector('button[name="remove_cart_item"]').click()
    driver.refresh()
    driver.find_element_by_css_selector('button[name="remove_cart_item"]').click()
    driver.refresh()
    driver.find_element_by_css_selector('button[name="remove_cart_item"]').click()
    driver.get("http://litecart/en/")
    time.sleep(5)
    





