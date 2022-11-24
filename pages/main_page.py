from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    url = 'https://www.asos.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    button_women = "//*[@id='women-floor']"
    choose_category_dresses = "//*[@id='chrome-sticky-header']/div[2]/div[1]/nav/div/div/button[4]"
    choose_category_party = "//*[@id='b2598144-62bd-4b68-804d-4cb894f853a1']/div/div[2]/ul/li[1]/ul/li[5]/a"
    choose_country_usa = "//button[@class='_1TlOB9h _2tvh469 _19qEA_b']"
    button_update_preferences = "//button[@data-testid='save-country-button']"
    choose_color = "//li[@data-dropdown-id='base_colour']"
    choose_color_black = "//*[@id='mediumRefinements']/li[7]/div/div/div/ul/li[1]/div/label/div[2]"
    main_word = "//*[@id='category-banner-wrapper']/div/h1"
    product = "//*[@id='product-203253951']/a/div[2]/div/div/h2"
    select_size = "//select[@id='main-size-select-0']"
    add_to_cart = "//button[@id='product-add-button']"


    #Getters

    def get_button_women(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_women)))

    def get_choose_category_dresses(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_category_dresses)))

    def get_choose_category_party(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_category_party)))

    def get_choose_country_usa(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_country_usa)))

    def get_button_update_preferences(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_update_preferences)))

    def get_choose_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_color)))

    def get_choose_color_black(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_color_black)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))


    #Actions

    def click_button_women(self):
        self.get_button_women().click()
        print("Click button women")

    def click_choose_category_dresses(self):
        self.get_choose_category_dresses().click()
        print("Click category")

    def click_choose_category_party(self):
        self.get_choose_category_party().click()
        print("Click dresses")

    def click_choose_country_usa(self):
        self.get_choose_country_usa().click()
        print("Click choose country")

    def click_button_update_preferences(self):
        self.get_button_update_preferences().click()
        print("Click choose country")

    def click_choose_color(self):
        self.get_choose_color().click()
        print("Click choose color")

    def click_choose_color_black(self):
        self.get_choose_color_black().click()
        print("Click choose color Black")

    def click_product(self):
        self.get_product().click()
        print("Click product")

    def click_select_size(self):
        self.get_select_size().click()
        print("Click button Size")

    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Add to cart")


    # Methods
    def category(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_women()
        self.driver.refresh()
        self.click_choose_country_usa()
        self.click_button_update_preferences()
        self.click_choose_category_dresses()
        self.click_choose_category_party()
        self.click_choose_color()
        self.click_choose_color_black()
        self.driver.refresh()
        self.assert_word(self.get_main_word(), "Party Dresses")
        self.click_product()
        self.click_select_size()
        self.driver.find_element(By.XPATH, self.select_size).send_keys(Keys.DOWN*5)
        self.driver.find_element(By.XPATH, self.select_size).send_keys(Keys.RETURN)
        self.get_screenshot()
        self.click_add_to_cart()



