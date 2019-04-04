import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(scope='session', autouse=True)
def driver(request):
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    # wd = webdriver.Firefox(capabilities={"marionette": False}, firefox_binary={"c:\\Program Files (x86)\\Nightly\\firefox.exe"})
    wd = webdriver.Chrome()
    #driver.implicitly_wait(10)
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd

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
            'text-decoration-line') == 'line-through'
        assert price_pp == price_hp in attr_product_hp
        price_discount_pp = driver.find_element_by_css_selector('strong.campaign-price').get_attribute('innerText')
        assert driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property(
            'color') == 'rgba(204, 0, 0, 1)'
        assert driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property(
            'font-weight') >= '700'
        font_size_price_pp = driver.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size')
        font_size_price_discount_pp = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size')
        assert int(font_size_price_pp[0:2]) < int(font_size_price_discount_pp[0:2])
        assert price_discount_pp == price_discount_hp in attr_product_hp
