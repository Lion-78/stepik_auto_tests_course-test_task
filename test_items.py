from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_has_btn_add_to_basket(browser):
    browser.get(link)
    # add_to_basket_btn = browser.find_element_by_css_selector("button.btn-add-to-basket")
    add_to_basket_btn = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_to_basket_btn is not None, "This page doesn't contain 'Add to basket' button!"
