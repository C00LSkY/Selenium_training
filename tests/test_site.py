from tests.authorization import *



def test_sticker_presents(driver):
    auth(driver)
    # поиск всех картинок товара
    list_image = driver.find_elements_by_css_selector('.product .image')
    # количество стикеров
    sticker = driver.find_elements_by_css_selector('ul.listing-wrapper.products .sticker')
    assert int(len(sticker)) == int(len(list_image))

def test_product_page(driver):
    auth(driver)
    pass