*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
Verify login scenario with valid credentials
    Open Browser    ${url}    firefox
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://input[@name='username']
    Input Text    xpath://input[@name='username']    admin

    Input Text    xpath://input[@name='password']    admin123

    Click Element    xpath://button[@type='submit']

    Wait Until Element Is Visible    xpath://h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']
    Element Should Be Visible    xpath://h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']

    Close Browser
