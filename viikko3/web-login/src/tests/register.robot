*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser


*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page and Check Page
    Set Username  kalle
    Set Password  kalle123
    Set Confirm Password  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page and Check Page
    Set Username  ka
    Set Password  kalle123
    Set Confirm Password  kalle123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Invalid Password
    Go To Register Page and Check Page
    Set Username  kalle
    Set Password  kalle
    Set Confirm Password  kalle
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Go To Register Page and Check Page
    Set Username  kalle
    Set Password  kalle123
    Set Confirm Password  kalle456
    Submit Credentials
    Register Should Fail With Message  Passwords do not match


*** Keywords ***
Go To Register Page and Check Page
    Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Welcome Page Should Be Open

Set Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Submit Credentials
    Click Button  Register
