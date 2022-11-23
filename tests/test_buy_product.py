import time
import pytest

from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
# from pages.client_inf_page import Client_information_page
# from pages.finish_page import Finish_page
# from pages.payment_page import Payment_page
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\komar\\PycharmProjects\\Resource\\chromedriver.exe', chrome_options=options)
    print("Start test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.category()

    time.sleep(5)

    # cp = Cart_page(driver)
    # cp.go_to_cart()
    #
    # cip = Client_information_page(driver)
    # cip.input_information()
    #
    # p = Payment_page(driver)
    # p.click_finish_button()
    #
    # f = Finish_page(driver)
    # f.finish()


    print("Finish test")
    time.sleep(4)
    driver.quit()





