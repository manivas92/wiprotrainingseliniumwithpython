import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class Test_Frame:
    def test_frame(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)
        driver.switch_to.frame(0)

        datepicker = driver.find_element(By.XPATH,"//input[@id='datepicker']")
        datepicker.click()
        driver.close()
