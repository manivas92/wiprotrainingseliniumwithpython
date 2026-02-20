*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
verify login with valid credentials
                   Login
    
verify Add to cart functionality
                   Login
    Log        User selects the product
    Log        User adds the product to the cart
    Log        User verifies that the product with details is added to cart
    
*** Keywords ***
Login 
    Log        Enter username
    Log        Enter password    
    Log        click on login button
    Log        user is on the home page     