*** Settings ***
Suite Setup       SetUp
Suite Teardown    Close All Browsers
Library           Selenium2Library
Library           String
Library           Search_suite_functions/Date.py
Library           Search_suite_functions/Boxes.py
Library           Search_suite_functions/StockNumberAndChangeAndVolume.py
Library           Search_suite_functions/VerifyTitle.py
Library           Search_suite_functions/ClickDropDownItem.py
Library           Search_suite_functions/VerifyPageNotEmpty.py

*** Variables ***
${url}            https://localhost:3000/
@{credentials}    mrkhedma@gmail.com    12345
${browser}        chrome
${add_to_portfolio_stock_number}    8
@{companies}      ATB    BIAT    ARTES RENAULT
${dropdown_item}    xpath=//button[@class='dropdown-item']
${company_chart}    id=companyChart
${start_trading_now_btn}    xpath=//button[contains(text(),'Start Trading Now')]
${popup_tag}      tag=app-broker-popup
${avatrade_src}    xpath=//img[@src='https://pbs.twimg.com/profile_images/877054364980039682/folYyr1B.jpg']
${avatrade_url}    https://www.avatrade.com/?tag=85712
${questrade_src}    xpath=//img[@src='https://www.questrade.com/images/librariesprovider11/default-album/logos/questrade-logo-reversed.svg']
${questrade_url}    https://www.questrade.com/?refid=qvatvy4y
${date_element_xpath}    xpath=//div[contains(text(),'Currency in USD ')]
${stocknumber_change_volume_class}    class=f_2
${add_to_portfolio_btn}    xpath=//span[contains(text(),'Add to portfolio')]
${add_to_portfolio_field}    class=finispia-input
${add_to_portfolio_add_btn}    class=apply-add-stock
${add_to_portfolio_popover}    class=popover-content
${add_to_portfolio_cancel_btn}    class=cancel-add-stock
${boxes_class}    class=box
${boxes_question_mark_class}    class=why-fail
${boxes_popover_class}    class=popover-content
${popup_cancel_btn}    xpath=//button[@class='close pull-right']
${title_tag}      tag=h4
${search_field}    xpath=//input[@name='company']
${login_link}     link=Log in
${email_field}    id=emailField
${password_field}    id=password
${search_by_company_btn}    link=Search by Company
${advanced_search_btn}    link=Advanced Search
${login_btn}      class=btn
${search_url}     https://localhost:3000/company/search

*** Test Cases ***
Verify Search Elements Test
    Login
    : FOR    ${company}    IN    @{companies}
    \    log    ****** starting verification of ${company} *****
    \    Input Text    ${search_field}    ${company}
    \    ${is_drop_down_item_clicked}    isDropDownItemClicked
    \    Run keyword And Continue On Failure    Should Not Be Equal    ${is_drop_down_item_clicked}    ${False}
    \    Continue For Loop If    ${is_drop_down_item_clicked} is ${False}
    \    Sleep    10
    \    ${page_is_empty}    verifyPageNotEmpty
    \    Run keyword And Continue On Failure    Should Not Be Equal    ${page_is_empty}    ${True}
    \    Continue For Loop If    ${page_is_empty} is ${True}
    \    Run keyword And Continue On Failure    VerifyTitle    ${company}
    \    ${title_not_equal_to previous_company}    Title    ${title_tag}    ${company}
    \    Continue For Loop If    ${title_not_equal_to_previous_company} is ${False}
    \    Run keyword And Continue On Failure    verifyCloseDate    ${date_element_xpath}
    \    Run keyword And Continue On Failure    stockNumberAndchangeAndvolumeVerification    ${stocknumber_change_volume_class}
    \    Run keyword And Continue On Failure    Page Should Contain Element    ${company_chart}
    \    Run keyword And Continue On Failure    VerifyAddToPortfolio
    \    Run keyword And Continue On Failure    boxesVerification    ${boxes_class}    ${boxes_question_mark_class}    ${boxes_popover_class}
    \    Run keyword And Continue On Failure    VerifyStartTradingNowBtn
    \    Log    ****** End of verification of ${company} *****



*** Keywords ***
Login
    Click Link    ${login_link}
    Wait Until Page Contains Element    ${email_field}
    input Text    ${email_field}    @{credentials}[0]
    input Password    ${password_field}    @{credentials}[1]
    Click Button    ${login_btn}
    Set Selenium Implicit Wait    30
    Page Should Not Contain Element    class=modal-content
    Run Keyword And Continue On Failure    Page Should Contain Element    ${search_by_company_btn}
    Run Keyword And Continue On Failure    Page Should Contain Element    ${advanced_search_btn}
    Run Keyword And Continue On Failure    Page Should Contain Element    ${search_field}
    ${locatoion}    Get Location
    Should Be Equal    ${locatoion}    ${search_url}

VerifyAddToPortfolio
    Click Element    ${add_to_portfolio_btn}
    Input Text    ${add_to_portfolio_field}    ${add_to_portfolio_stock_number}
    Textfield Value Should Be    ${add_to_portfolio_field}    ${add_to_portfolio_stock_number}
    Click Button    ${add_to_portfolio_add_btn}
    Page Should Not Contain Element    ${add_to_portfolio_popover}
    Click Element    ${add_to_portfolio_btn}
    Textfield Value Should Be    ${add_to_portfolio_field}    ${add_to_portfolio_stock_number}
    Comment    ${resultat}    Get Element Attribute    ${add_to_portfolio_field}    value
    Comment    Should Be Equal    ${resultat}    ${add_to_portfolio_stock_number}
    Click Button    class=cancel-add-stock
    Comment    On clique plusieurs fois sur le bouton Add pour verifier plus tard si l'element s'ajoute plusieurs fois dans le portfolio
    Click Element    ${add_to_portfolio_btn}
    Click Button    ${add_to_portfolio_add_btn}
    Click Element    ${add_to_portfolio_btn}
    Click Button    ${add_to_portfolio_add_btn}

SetUp
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

VerifyTradePages
    [Arguments]    ${src}    ${page_url}
    Set Focus To Element    ${popup_tag}
    Click Element    ${src}
    Select Window    url=${page_url}
    ${location}    Get Location
    Should Be Equal    ${location}    ${page_url}
    Select Window    title=Finispia

VerifyStartTradingNowBtn
    Run Keyword And Ignore Error    Click Button    ${start_trading_now_btn}
    Page Should Contain Element    ${popup_tag}
    Run keyword And Continue On Failure    VerifyTradePages    ${avatrade_src}    ${avatrade_url}
    Run keyword And Continue On Failure    VerifyTradePages    ${questrade_src}    ${questrade_url}
    Set Focus To Element    ${popup_tag}
    Click Button    ${popup_cancel_btn}

VerifyTitle
    [Arguments]    ${company_name}
    ${title}    Get Text    ${title_tag}
    Should Be Equal    ${title}    ${company_name}
