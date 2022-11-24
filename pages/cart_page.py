from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    cart = "//div[@id='miniBagDropdown']"
    checkout_button = "//*[@id='minibag-dropdown']/div/div/div/div[2]/div/div[3]/div[2]/a"


    #Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    #Actions

    def click_cart(self):
        self.get_cart().click()
        print("Click cart button")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")

    # Methods
    def go_to_cart(self):
        self.get_current_url()
        self.click_cart()
        self.click_checkout_button()





