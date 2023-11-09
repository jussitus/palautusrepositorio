*** Settings ***
Resource            resource.robot
Resource            login_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser


*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page and Check Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${GOOD_PASSWORD}
    Set Confirm Password  ${GOOD_PASSWORD}
    Submit Credentials  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page and Check Page
    Set Username  ${BAD_USERNAME_SHORT}
    Set Password  ${GOOD_PASSWORD}
    Set Confirm Password  ${GOOD_PASSWORD}
    Submit Credentials  Register
    Register Should Fail With Message  Invalid username

Register With Valid Username And Invalid Password
    Go To Register Page and Check Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${BAD_PASSWORD_ONLY_LETTERS}
    Set Confirm Password  ${BAD_PASSWORD_ONLY_LETTERS}
    Submit Credentials  Register
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Go To Register Page and Check Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${GOOD_PASSWORD}
    Set Confirm Password  ${GOOD_PASSWORD}1
    Submit Credentials  Register
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Go To Register Page and Check Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${GOOD_PASSWORD}
    Set Confirm Password  ${GOOD_PASSWORD}
    Submit Credentials  Register
    Register Should Succeed
    Click Link  ohtu
    Click Button  Logout
    Go To Login Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${GOOD_PASSWORD}
    Submit Credentials  Login
    Login Should Succeed

Login After Failed Registration
    Go To Register Page and Check Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${BAD_PASSWORD_ONLY_LETTERS}
    Set Confirm Password  ${BAD_PASSWORD_ONLY_LETTERS}
    Submit Credentials  Register
    Register Should Fail With Message  Invalid password
    Go To Login Page
    Set Username  ${GOOD_USERNAME}
    Set Password  ${GOOD_PASSWORD}
    Submit Credentials  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Go To Register Page and Check Page
    Reset Application
    Go To Register Page
    Register Page Should Be Open
