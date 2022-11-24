from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):

    url = 'https://www.asos.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    username = "//input[@name='Username']"
    password = "//input[@name='Password']"
    sigh_in_button = "//input[@id='signin']"


    # Getters

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_sigh_in_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sigh_in_button)))


    # Actions

    def input_username(self, username):
        self.get_username().send_keys(username)
        print("Input username")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_sigh_in_button(self):
        self.get_sigh_in_button().click()
        print("Click Sigh in button")

    # Methods

    def authorization(self):

        self.get_current_url()
        self.input_username("qa2323@yahoo.com")
        self.input_password("Qa1234567!")
        self.click_sigh_in_button()




