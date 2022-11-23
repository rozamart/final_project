import datetime
from selenium import webdriver
# from selenium.webdriver import ActionChains
# driver = webdriver.Chrome(executable_path='C:\\Users\\komar\\PycharmProjects\\Resourse\\chromedriver.exe')

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\komar\\PycharmProjects\\Project_shopping\\Screen\\' + name_screenshot)

    # """Method assert url"""
    #
    # def assert_url(self, result):
    #     get_url = self.driver.current_url
    #     assert get_url == result
    #     print("Good URL")

