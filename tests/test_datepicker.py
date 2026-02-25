import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_RS_DatePicker:

    def test_select_date(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        driver.get("https://rsuitejs.com/components/date-picker/")

        driver.execute_script("window.scrollBy(0,600)")

        date_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//input[contains(@class,'rs-input')])[1]"))
        )
        date_input.click()

        header = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'rs-calendar-header-title')]"))
        )
        header.click()

        year = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='2025']"))
        )
        year.click()

        month = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Mar']"))
        )
        month.click()

        day = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='15']"))
        )
        day.click()

        time.sleep(3)
        driver.quit()