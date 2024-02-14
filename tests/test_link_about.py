from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
sys.path.append("C:\\Users\\Rafkat\\Desktop\\Selenium\\finalproject")
from pages.login_page import Login_page
from webdriver_manager.chrome import ChromeDriverManager



def test_link_about():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("Start Test")

    login = Login_page(driver)
    login.authorisation()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish Test")
    time.sleep(10)
    driver.quit()



   
    



