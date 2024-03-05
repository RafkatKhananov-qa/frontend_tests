from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.google_main_page import Google_main_page
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def test_search_google():
    # options = Options()
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.headless = True
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    start_page = Google_main_page(driver)
    start_page.search_information("546547657567rhffdhbfddfhdfhfdbfbbbdf")

    time.sleep(3)
    text_google = driver.find_element(By.XPATH, "//p[@aria-level='3' and text()='По запросу ']")
    value_text = text_google.text
    assert value_text == "По запросу 546547657567rhffdhbfddfhdfhfdbfbbbdf ничего не найдено. "
    driver.quit()
