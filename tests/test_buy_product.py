import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
import sys
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.login_page import Login_page
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.mark.order(3)
def test_buy_product_1():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    print("Start Test 1")

    login = Login_page(driver)
    login.authorisation()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_information()

    pay = Payment_page(driver)
    pay.payment()

    f = Finish_page(driver)
    f.finish()


    print("Finish Test 1")
    # time.sleep(10)
    driver.quit()


@pytest.mark.order(1)
def test_buy_product_2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 2")

    login = Login_page(driver)
    login.authorisation()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()


    print("Finish Test 2")
    # time.sleep(10)
    driver.quit()




# @pytest.mark.order(2)
def test_buy_product_3():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    print("Start Test 3")

    login = Login_page(driver)
    login.authorisation()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()


    print("Finish Test 3")
    # time.sleep(10)
    driver.quit()






