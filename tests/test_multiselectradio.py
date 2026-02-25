import time
from itertools import count

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_radio():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    checkbox_list = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    count = len(checkbox_list)
    print(count)

    for i in checkbox_list:
        time.sleep(2)
        i.click()

    driver.close()
