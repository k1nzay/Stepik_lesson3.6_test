from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']//button[@type='submit']")
