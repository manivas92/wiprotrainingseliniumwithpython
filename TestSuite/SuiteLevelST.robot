*** Settings ***
#settings add the external library details , resources , setup and teardown commands
Resource        Resource.robot
Library        SeleniumLibrary
Suite Setup            Open DB
Suite Teardown            Log    Close DB

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
                Login

Verify Add to cart functionality
                Login
    Log     User selects the product
    Log     User add the product to the cart
    Log     User verifies that the product with details is added to cart