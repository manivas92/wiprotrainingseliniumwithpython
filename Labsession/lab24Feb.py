import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_DemoWebShop:

    def test_register_login_order_cod(self):

        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        time.sleep(2)

        # ---------------- REGISTER ----------------
        driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)

        driver.find_element(By.ID, "gender-male").click()
        driver.find_element(By.ID, "FirstName").send_keys("Manivas")
        driver.find_element(By.ID, "LastName").send_keys("T")

        email = f"testuser{int(time.time())}@gmail.com"
        driver.find_element(By.ID, "Email").send_keys(email)

        driver.find_element(By.ID, "Password").send_keys("Test@123")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("Test@123")

        driver.find_element(By.ID, "register-button").click()
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "Log out").click()
        time.sleep(2)

        # ---------------- LOGIN ----------------
        driver.find_element(By.LINK_TEXT, "Log in").click()
        time.sleep(2)

        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys("Test@123")
        driver.find_element(By.XPATH, "//input[@value='Log in']").click()
        time.sleep(3)

        # ---------------- ADD PRODUCT TO CART ----------------
        driver.find_element(By.LINK_TEXT, "Books").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()
        time.sleep(3)

        driver.find_element(By.LINK_TEXT, "Shopping cart").click()
        time.sleep(2)

        driver.find_element(By.ID, "termsofservice").click()
        driver.find_element(By.ID, "checkout").click()
        time.sleep(3)

        # ---------------- CHECKOUT PROCESS ----------------

        # Billing Address
        Select(driver.find_element(By.ID, "BillingNewAddress_CountryId")).select_by_visible_text("India")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Hyderabad")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Madhapur")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("500081")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("9876543210")
        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()
        time.sleep(3)

        # Shipping
        driver.find_element(By.XPATH, "//input[@onclick='Shipping.save()']").click()
        time.sleep(2)

        # Shipping Method
        driver.find_element(By.XPATH, "//input[@onclick='ShippingMethod.save()']").click()
        time.sleep(2)

        # Payment Method (Cash On Delivery)
        driver.find_element(By.XPATH, "//input[@value='Payments.CashOnDelivery']").click()
        driver.find_element(By.XPATH, "//input[@onclick='PaymentMethod.save()']").click()
        time.sleep(2)

        # Payment Info
        driver.find_element(By.XPATH, "//input[@onclick='PaymentInfo.save()']").click()
        time.sleep(2)

        # Confirm Order
        driver.find_element(By.XPATH, "//input[@onclick='ConfirmOrder.save()']").click()
        time.sleep(5)

        # Verify Order Success
        success = driver.find_element(By.XPATH, "//strong[contains(text(),'Your order has been successfully processed!')]")
        assert "successfully processed" in success.text

        print("Order placed successfully!")

        time.sleep(3)
        driver.quit()