from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import Main_page
from pages.login_page import Login_page
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def test_link_about():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    print("Start Test")

    login = Login_page(driver)
    login.authorisation()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish Test")
    time.sleep(10)
    driver.quit()



   
    



