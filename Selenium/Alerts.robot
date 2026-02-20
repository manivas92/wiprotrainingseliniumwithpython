*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Verify drop downs
    Open Browser    ${url}    firefox

    # maximize the browser window
    Maximize Browser Window

    Wait Until Element Is Visible    xpath:(//button)[1]
    Click Element    xpath:(//button)[1]

# Informational alert - ACCEPT is for OK button
    Handle Alert    action=ACCEPT    timeout=3

    Wait Until Element Is Visible    xpath:(//button)[2]
    Click Element    xpath:(//button)[2]

# Confirmation alert - ACCEPT is for OK button, DISMISS is for Cancel button
    Handle Alert    action=DISMISS    timeout=3

    Wait Until Element Is Visible    xpath:(//button)[3]
    Click Element    xpath:(//button)[3]

# Prompt alert - Enter text and accept
    Input Text Into Alert    Hello
    Handle Alert    action=ACCEPT    timeout=3

    Close Browser
