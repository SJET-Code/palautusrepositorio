*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pelle
    Set Password  hermann1
    Set Password Confirmation  hermann1
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  pe
    Set Password  hermann1
    Set Password Confirmation  hermann1
    Submit Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  pelle
    Set Password  hermanni
    Set Password Confirmation  hermanni
    Submit Register
    Register Should Fail With Message  Password must contain non-letter characters

Register With Nonmatching Password And Password Confirmation
    Set Username  pelle
    Set Password  hermann1
    Set Password Confirmation  hermann!
    Submit Register
    Register Should Fail With Message  The passwords differ

Login After Successful Registration
    Set Username  pelle
    Set Password  hermann1
    Set Password Confirmation  hermann1
    Submit Register
    Go To Login Page
    Set Username  pelle
    Set Password  hermann1
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  pelle
    Set Password  hermanni
    Set Password Confirmation  hermanni
    Submit Register
    Register Should Fail With Message  Password must contain non-letter characters
    Go To Login Page
    Login Page Should Be Open
    Set Username  pelle
    Set Password  hermanni
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

