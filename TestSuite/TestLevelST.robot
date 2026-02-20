*** Settings ***
#settings add the external library details , resources , setup and teardown commands
Library        SeleniumLibrary
Resource        Resource.robot
Test Setup        Log        Launch Browser
Test Teardown        Log        Close the Browser

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
                Login

Verify Add to cart functionality
                Login
    Log     User selects the product
    Log     User add the product to the cart
    Log     User verifies that the product with details is added to cart