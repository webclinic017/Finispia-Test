*** Settings ***
Suite Setup       SetUp
Suite Teardown    Close All Browsers
Library           Selenium2Library
Library           Subscription_functions/GetRandomEmail.py

*** Variables ***
${url}            https://localhost:3000/
${browser}        chrome

*** Test Cases ***
SubscriptionTest
    EnterSubscription
    EmptyCredentials
    Reload Page
    InvalidEmail
    Reload Page
    AlreadyUsedEmail
    Reload Page
    OnlyEmail
    Reload Page
    NotMatchingPasswords
    Reload Page
    ValidSubscription
    log    ******************************
    EnterSubscription
    Run Keyword And Continue On Failure    EmptyCredentials
    Run Keyword And Continue On Failure    InvalidEmail
    Run Keyword And Continue On Failure    AlreadyUsedEmail
    Run Keyword And Continue On Failure    NotMatchingPasswords
    Run Keyword And Continue On Failure    OnlyEmail
    Run Keyword And Continue On Failure    ValidSubscription

*** Keywords ***
EmptyCredentials
    log    ***** Empty Credentials Verification *****
    ClearTextFields
    Click Button    class=btn
    Page Should Contain    A valid email is required
    Page Should Contain    Password is required

InvalidEmail
    log    ***** Invalid Email Verification *****
    ClearTextFields
    Input Text    id=emailField    Invalid Email
    Input Password    id=password    password
    Input Password    id=repeatpassword    password
    Click Button    class=btn
    Page Should Contain    A valid email is required

AlreadyUsedEmail
    log    ***** Already used email verification *****
    ClearTextFields
    Input Text    id=emailField    dorra.chaari@enis.tn
    Input Password    id=password    password
    Input Password    id=repeatpassword    password
    Click Button    class=btn
    Wait Until Keyword Succeeds    10    2    Page Should Contain    Account already exists

OnlyEmail
    log    ***** Only email Verification *****
    ClearTextFields
    ${random_valid_email}    getRandomValidEmail
    Input Text    id=emailField    ${random_valid_email}
    Click Button    class=btn
    Page Should Contain    Password is required

SetUp
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

NotMatchingPasswords
    log    ***** Not Matching Passwords *****
    ClearTextFields
    Input Text    id=emailField    test@iovision.tn
    Input Password    id=password    password
    Input Password    id=repeatpassword    other_password
    Click Button    class=btn
    Page Should Contain    Password does not match the confirm password.

ValidSubscription
    log    ***** valid Subscription verification *****
    ClearTextFields
    ${random_valid_email}    getRandomValidEmail
    Input Text    id=emailField    ${random_valid_email}
    Input Password    id=password    password
    Input Password    id=repeatpassword    password
    Click Button    class=btn
    Wait Until Keyword Succeeds    20    10    Page Should Contain Element    class=modal-content
    Set Focus To Element    class=modal-content
    Click Link    link=ok
    sleep    5

EnterSubscription
    Click Link    link=Subscription Plan
    Click Element    tag=button
    sleep    5
    ${location}    Get Location
    Should Be Equal    ${location}    https://localhost:3000/login/signin?plan=FREE&remember=

ClearTextFields
    Clear Element Text    id=emailField
    Clear Element Text    id=password
    Clear Element Text    id=repeatpassword
