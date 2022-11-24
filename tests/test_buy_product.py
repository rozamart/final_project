import time
import pytest
import undetected_chromedriver as uc

from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.finish_page import Finish_page
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\komar\\PycharmProjects\\Resource\\chromedriver.exe', chrome_options=options)
    driver = uc.Chrome()
    driver.get("https://asos.com")
    print("Start test")

    mp = Main_page(driver)
    mp.category()

    time.sleep(5)

    cp = Cart_page(driver)
    cp.go_to_cart()

    login = Login_page(driver)
    login.authorization()

    f = Finish_page(driver)
    f.finish()

    print("Finish test")

    time.sleep(4)
    driver.quit()





