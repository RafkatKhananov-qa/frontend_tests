from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Google_main_page(Base):

    url = 'https://www.google.com/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    search_input = "//textarea[@id='APjFqb']"
    search_button = "//input[@class='gNO89b']"
    
    
    # Getters

    def get_search_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_input)))
    
    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))
    

    # Actions
     
    def input_search(self, search_input):
        self.get_search_input().send_keys(search_input)
        print("Input search")
    
    def click_search_button(self):
        self.get_search_button().click()
        print("Click search button")
    

    # Methods 

    def search_information(self, search_input):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.input_search(search_input)
        self.click_search_button()


       