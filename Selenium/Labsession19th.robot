*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/check-box.php
*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser    ${url}    firefox
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://input[@id='c_bs_1']

    Click Element    xpath://input[@id='c_bs_1']
    sleep    5s
    Wait Until Element Is Visible    xpath://input[@id='c_bs_2']

    Click Element    xpath://input[@id='c_bs_2']
    Sleep    5s
    Close Browser