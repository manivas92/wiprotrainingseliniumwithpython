*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php

*** Test Cases ***
Select state and city
    Open Browser        ${url}        firefox
    Maximize Browser Window
    Select From List By Label    id:state    Uttar Pradesh

    Sleep    2 s

    # After state selected, city dropdown appears
    Select From List By Label    id:city    Lucknow

    Sleep    2s

    Close Browser