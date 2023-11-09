*** Settings ***
Resource    resource.robot
Library     SeleniumLibrary
Library     ../AppLibrary.py


*** Variables ***
${GOOD_USERNAME}                kalle
${BAD_USERNAME_SHORT}           ka
${GOOD_PASSWORD}                kalle123
${BAD_PASSWORD_SHORT}           kal123
${BAD_PASSWORD_ONLY_LETTERS}    kalleyykaakoo
${SOME_PASSWORD}                 salasana123


*** Keywords ***
Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

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
    [Arguments]  ${button}
    Click Button  ${button}