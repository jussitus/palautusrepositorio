*** Settings ***
Resource            resource.robot
Resource            login_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Create User And Go To Login Page


*** Test Cases ***
Login With Correct Credentials
    Set Username  ${GOOD_USERNAME}
    Set Password  ${GOOD_PASSWORD}
    Submit Credentials  Login
    Login Should Succeed

Login With Incorrect Password
    Set Username  ${GOOD_USERNAME}
    Set Password  ${SOME_PASSWORD}
    Submit Credentials  Login
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Reset Application
    Go To Login Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${GOOD_PASSWORD}
    Submit Credentials  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Create User And Go To Login Page
    Create User  ${GOOD_USERNAME}  ${GOOD_PASSWORD}
    Go To Login Page
    Login Page Should Be Open
