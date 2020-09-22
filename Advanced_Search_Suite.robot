*** Settings ***
Suite Setup       SetUp
Suite Teardown    Close All Browsers
Library           Selenium2Library
Library           String
Library           Advanced_search_suite_functions/SelectCountry.py
Library           Advanced_search_suite_functions/VerifyResults.py
Library           Advanced_search_suite_functions/GetNumberPages.py
Library           Advanced_search_suite_functions/AddToPortfolioBtn.py
Library           Advanced_search_suite_functions/VerifyPrice.py
Library           Advanced_search_suite_functions/VerifySectorsAndIndustries.py
Library           Advanced_search_suite_functions/VerifyFilters.py

*** Variables ***
@{credentials}    mrkhedma@gmail.com    12345
${search_field}    xpath=//input[@name='company']
${login_link}     link=Log in
${email_field}    id=emailField
${password_field}    id=password
${search_by_company_btn}    link=Search by Company
${advanced_search_btn}    link=Advanced Search
${login_btn}      class=btn
${find_stocks_btn}    class=btn
${combobox}       xpath=//span[@role='combobox']
${add_to_portfolio_btn}    xpath=//tr[1]/td[1]/button[1]
${add_to_portfolio_popover}    class=popover-content
${add_to_portfolio_input_field}    xpath=/html[1]/body[1]/popover-container[1]/div[2]/div[2]/input[1]
${add_to_portfolio_add_btn}    class=apply-add-stock
${filters_btn}    xpath=//span[contains(text(),'+ Set your own filter')]
${filters_popover}    class=popover-content
${search_url}     https://localhost:3000/company/search
${url}            https://localhost:3000
${browser}        chrome

*** Test Cases ***
VerifyStocksTest
    Login
    Wait Until Keyword Succeeds    30    5    Click link    ${advanced_search_btn}
    selectCountry    Tunisia
    Click Button    ${find_stocks_btn}
    Page Should not Contain    class=modal-body
    ${halal}    Set Variable    ${False}
    log    ******** Add to Portfolio Button Verification ********
    Run Keyword And Continue On Failure    VerifyAddToPortFolioBtn
    log    ******** Find Stocks Btn Verification ********
    Run Keyword And Continue On Failure    VerifyFindStocksBtn    ${halal}
    log    ******** Find only halal stocks checkbox Verification ********
    ${halal}    Set Variable    ${True}
    Run Keyword And Continue On Failure    VerifyOnlyHalalCheckbox    ${halal}
    ${halal}    Set Variable    ${False}
    log    ******** Price Verification ********
    Run Keyword And Continue On Failure    VerifyPrices
    log    ******** Sectors and Indestries Verification ********
    Run Keyword And Continue On Failure    verifySectorsAndIndustries
    log    ******** Filters Verification ********
    Run Keyword And Continue On Failure    VerifyFilterCheckboxes

*** Keywords ***
SetUp
    Open Browser    ${url}    ${browser}
    Maximize Browser Window
    Set Selenium Implicit Wait    30

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

VerifyAdvancedSearchResults
    [Arguments]    ${page_number}    ${halal}
    log    *****Page number ${page_number}*****
    ${result}    verifyResults    ${halal}
    Run Keyword If    ${result}    log    ===== Page Number ${page_number} rows are all accurate =====
    ...    ELSE    log    ===== Page Number ${page_number} rows are NOT accurate =====

VerifyFindStocksBtn
    [Arguments]    ${halal}
    @{pagination_numbers}    getNumberPages
    VerifyAdvancedSearchResults    1    ${halal}
    : FOR    ${i}    IN    @{pagination_numbers}
    \    Click Element    xpath=//a[contains(text(),'${i}')]
    \    sleep    5
    \    Comment    Wait Until Keyword Succeeds    20    5    Page Should Not Contain    class=app_loading
    \    VerifyAdvancedSearchResults    ${i}    ${halal}

VerifyAddToPortFolioBtn
    clickAddToPortfolioBtn    ${add_to_portfolio_btn}
    Page Should Not Contain Element    tag=modal-container
    Page Should Contain Element    ${add_to_portfolio_popover}
    Set Focus To Element    ${add_to_portfolio_popover}
    ${random_int} =    Evaluate    random.randint(0, 100)    modules=random
    ${unicode_random_int} =    Evaluate    unicode(${random_int})
    Input Text    ${add_to_portfolio_input_field}    ${unicode_random_int}
    Textfield Value Should Be    ${add_to_portfolio_input_field}    ${unicode_random_int}
    Click Button    ${add_to_portfolio_add_btn}
    Page Should Not Contain Element    ${add_to_portfolio_popover}
    clickAddToPortfolioBtn    ${add_to_portfolio_btn}
    Page Should Contain Element    ${add_to_portfolio_popover}
    Set Focus To Element    ${add_to_portfolio_popover}
    Textfield Value Should Be    ${add_to_portfolio_input_field}    ${unicode_random_int}

VerifyOnlyHalalCheckbox
    [Arguments]    ${halal}
    Select Checkbox    css=[type='checkbox']
    Click Button    ${find_stocks_btn}
    sleep    2
    VerifyFindStocksBtn    ${halal}
    Unselect Checkbox    css=[type='checkbox']
    Click Button    ${find_stocks_btn}
    sleep    2

VerifyPrices
    ${prices}    getAllPrices
    ${random_price}    getRandomPrice    ${prices}
    Run Keyword And Continue On Failure    Input Text    tag=input    ${random_price}
    Run Keyword And Continue On Failure    Click Button    ${find_stocks_btn}
    sleep    2
    ${link}    Set Variable    Greater than
    Run Keyword And Continue On Failure    VerifyOperande    ${link}    ${random_price}
    Run Keyword And Continue On Failure    Click Link    link=${link}
    Run Keyword And Continue On Failure    Page Should Contain Element    id=basic-link-dropdown
    Run Keyword And Continue On Failure    Set Focus To Element    id=basic-link-dropdown
    ${link}    Set Variable    Equal
    Run Keyword And Continue On Failure    Click Link    link=${link}
    Run Keyword And Continue On Failure    Click Button    ${find_stocks_btn}
    sleep    2
    Run Keyword And Continue On Failure    VerifyOperande    ${link}    ${random_price}
    Run Keyword And Continue On Failure    Click Link    link=${link}
    Run Keyword And Continue On Failure    Page Should Contain Element    id=basic-link-dropdown
    Run Keyword And Continue On Failure    Set Focus To Element    id=basic-link-dropdown
    ${link}    Set Variable    Less than
    Run Keyword And Continue On Failure    Click Link    link=${link}
    Run Keyword And Continue On Failure    Click Button    ${find_stocks_btn}
    sleep    2
    Run Keyword And Continue On Failure    VerifyOperande    ${link}    ${random_price}

getRandomPrice
    [Arguments]    ${prices}
    ${length} =    Get Length    ${prices}
    Should Not Be Equal    int(${length})    int(0)
    ${middle}    Evaluate    (${length}-1)//2
    Return From Keyword    ${prices}[${middle}]
    Comment    we take the middle of the list to make sure that there is at least on item greater and other less

VerifyThePriceElement
    [Arguments]    ${page_number}    ${link}    ${random_price}
    log    *****Page number ${page_number}*****
    ${result}    priceVerification    ${link}    ${random_price}
    Run Keyword If    ${result}    log    ===== Page Number ${page_number} rows are all accurate =====
    ...    ELSE    log    ===== Page Number ${page_number} rows are NOT accurate =====

VerifyOperande
    [Arguments]    ${link}    ${random_price}
    @{pagination_numbers}    getNumberPages
    VerifyThePriceElement    1    ${link}    ${random_price}
    : FOR    ${i}    IN    @{pagination_numbers}
    \    Click Element    xpath=//a[contains(text(),'${i}')]
    \    sleep    5
    \    Comment    Wait Until Keyword Succeeds    20    5    Page Should Not Contain    class=app_loading
    \    VerifyThePriceElement    ${i}    ${link}    ${random_price}

VerifyFilterCheckboxes
    Wait Until Keyword Succeeds    30    5    click element    ${filters_btn}
    Page Should Contain Element    ${filters_popover}
    ${number_filters}    getNumberFilters
    : FOR    ${i}    IN RANGE    1    ${number_filters+1}
    \    Run Keyword And Continue On Failure    Select Checkbox    xpath=/html[1]/body[1]/popover-container[1]/div[2]/div[1]/table[1]/tbody[1]/tr[${i}]/td[1]/input[1]
    \    ${result}    verifyFilterIsSelected    ${i}
    \    Run Keyword And Continue On Failure    Should Be Equal    ${result}    ${True}
