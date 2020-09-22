*** Settings ***
Suite Setup       SetUp
Suite Teardown    Close All Browsers
Library           Selenium2Library
Library           Manage_account_suite_functions/ManageAccountVerification.py

*** Variables ***
${url}            https://localhost:3000
${browser}        chrome
@{credentials}    mrkhedma@gmail.com    12345
${login_link}     link=Log in
${email_field}    id=emailField
${password_field}    id=password
${login_btn}      class=btn
${search_by_company_btn}    link = Search by Company
${advanced_search_btn}    link = Advanced Search
${search_field}    xpath=//input[@name='company']
${search_url}     https://localhost:3000/company/search
${profile_menu}    xpath=//a[@id='profileMenu']/div[@class='col-10 no-padding']
${profile_link}    link=Profile
${manage_account_url}    https://localhost:3000/customer/account
${password_link}    link=Password
${save_password_btn}    xpath=//button[contains(text(),'Save password')]
${menu}           class=no-padding
${logout_link}    link=Logout
${wrong_login_modal}    class=modal-content
${ok_btn}         link=ok
${logo}           class=logo
${test_password}    test_password

*** Test Cases ***
ChangePasswordTest
    Login
    ${old_password}    Set Variable    @{credentials}[1]
    ${new_password}    Set Variable    ${test_password}
    EnterProfile
    ChangeThePassword    ${old_password}    ${new_password}
    log    ****Starting Unsuccessful Login Verification *****
    Run Keyword And Continue On Failure    UnsuccessfulLogin
    log    ****Starting Successful Login Verification *****
    Run Keyword And Continue On Failure    SuccessfulLogin    ${new_password}
    log    ***** Resetting Password *****
    ResetPassword    ${old_password}    ${new_password}

*** Keywords ***
SetUp
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    60

Login
    Click Link    ${login_link}
    Wait Until Page Contains Element    ${email_field}
    input Text    ${email_field}    @{credentials}[0]
    input Password    ${password_field}    @{credentials}[1]
    Click Button    ${login_btn}
    Set Selenium Implicit Wait    60
    Page Should Not Contain Element    class=modal-content
    Run Keyword And Continue On Failure    Page Should Contain Element    ${search_by_company_btn}
    Run Keyword And Continue On Failure    Page Should Contain Element    ${advanced_search_btn}
    Run Keyword And Continue On Failure    Page Should Contain Element    ${search_field}
    ${locatoion}    Get Location
    Should Be Equal    ${locatoion}    ${search_url}

EnterProfile
    Run Keyword And Ignore Error    Page Should Contain Element    ${profile_menu}
    Mouse Over    ${profile_menu}
    Click Link    ${profile_link}
    sleep    10
    ${location}    Get Location
    Should Be Equal    ${location}    ${manage_account_url}

ChangeThePassword
    [Arguments]    ${old_password}    ${new_password}
    click link    ${password_link}
    changePassword    ${old_password}    ${new_password}
    Click Button    ${save_password_btn}
    sleep    10
    Comment    Make sure That the button has been successfully clicked
    Click Button    ${save_password_btn}
    sleep    10
    Run Keyword And Continue On Failure    Mouse Over    ${menu}
    Run Keyword And Continue On Failure    Click Link    ${logout_link}

UnsuccessfulLogin
    Click Link    ${login_link}
    Wait Until Page Contains Element    ${email_field}
    input Text    ${email_field}    @{credentials}[0]
    input Password    ${password_field}    @{credentials}[1]
    Click Button    ${login_btn}
    Page Should Contain Element    ${wrong_login_modal}
    Set Focus To Element    ${wrong_login_modal}
    Click Link    ${ok_btn}
    Wait Until Keyword Succeeds    20    5    Page Should not Contain Element    ${wrong_login_modal}

SuccessfulLogin
    [Arguments]    ${new_password}
    input Text    ${email_field}    @{credentials}[0]
    input Password    ${password_field}    ${new_password}
    Run Keyword And Ignore Error    Click Button    ${login_btn}
    Page Should Not Contain Element    ${wrong_login_modal}
    ${location}    Get Location
    Should Be Equal    ${location}    ${search_url}

ResetPassword
    [Arguments]    ${old_password}    ${new_password}
    ${location}    Get Location
    Click Image    ${logo}
    EnterProfile
    ChangeThePassword    ${new_password}    ${old_password}
    Login
    Page Should Not Contain Element    ${wrong_login_modal}
    log    Password is reseted successfully
