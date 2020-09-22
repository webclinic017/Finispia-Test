*** Settings ***
Suite Setup       SetUp
Suite Teardown    Close All Browsers
Library           Selenium2Library
Library           Portfolio_suite_functions/VerifyPortfolio.py
Library           Collections

*** Variables ***
${url}            https://localhost:3000/
@{credentials}    mrkhedma@gmail.com    12345
${browser}        chrome
${login_link}     link=Log in
${email_field}    id=emailField
${password_field}    id=password
${login_btn}      class=btn
${profile_menu}    xpath=//a[@id='profileMenu']/div[@class='col-10 no-padding']
${portfolio_link}    link=Portfolio
${portfolio_url}    https://localhost:3000/customer/portfolio
${edit_popover}    class=popover-content
${edit_input_field}    class=finispia-input
${edit_btn}       class=apply-add-stock
${profile_link}    link=Profile
${search_url}     https://localhost:3000/company/search
${search_by_company_btn}    link = Search by Company
${advanced_search_btn}    link = Advanced Search
${search_field}    xpath=//input[@name='company']

*** Test Cases ***
My portfolio Test
    EnterPortfolio
    log    *****Starting Portfolio is not Empty verification *****
    verifyMyPortfolioNotEmpty
    log    *****Starting Edit Buttoon Verification*****
    Run Keyword And Continue On Failure    VerifyEditButtons
    log    *****Starting POrtfolio contains no repeated rows verification*****
    VerifyPortfloioDontContainRepeatedRows

*** Keywords ***
SetUp
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    60

Login
    [Arguments]    ${email}    ${password}
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

EnterPortfolio
    Login    @{credentials}[0]    @{credentials}[1]
    Run Keyword And Ignore Error    Page Should Contain Element    ${profile_menu}
    Mouse Over    ${profile_menu}
    Page Should Contain Element    class=dropdown-menu
    Click Link    ${portfolio_link}
    sleep    10
    ${location}    Get Location
    Should Be Equal    ${location}    ${portfolio_url}
    Comment    Wait Until Element Is Not Visible    class=app_loading

VerifyEditButtons
    ${result}    getQuantityIndexAndLastElementIndex
    ${qte_index}    Set Variable    ${result}[0]
    ${last_element_index}    Set Variable    ${result}[1]
    ${old_qte}    Get Text    xpath=//tr[1]/td[${qte_index}]
    Click Element    xpath=//tr[1]/td[${last_element_index}]/span
    Page Should Contain Element    ${edit_popover}
    ${new_qte}    getRandomQuantity    ${old_qte}
    Input Text    ${edit_input_field}    ${new_qte}
    Click Button    ${edit_btn}
    sleep    15
    ${qte}    Get Text    xpath=//tr[1]/td[${qte_index}]
    Should Be Equal As Strings    ${new_qte}    ${qte}
