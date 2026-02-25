import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_login:
    def test_login(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.implicitly_wait(10)

        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()
        windows = driver.window_handles
        print(windows)
        driver.switch_to.window(windows[1])
        time.sleep(3)

        text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(text)
        driver.close()
        time.sleep(3)

        driver.switch_to.window(windows[0])
        clickhere.is_displayed()

        driver.close()