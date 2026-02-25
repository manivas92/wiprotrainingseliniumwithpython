import time
import pytest
from selenium.webdriver.common.by import By


class Test_Alerts:

    def test_alerts(self, driver):

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # Simple Alert
        simplealt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
        simplealt.click()
        alert = driver.switch_to.alert
        alert.accept()

        # Confirm Alert
        confalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
        confalt.click()
        alert = driver.switch_to.alert
        alert.dismiss()

        # Prompt Alert
        promptalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
        promptalt.click()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.send_keys("test hello")
        alert.accept()

        time.sleep(2)