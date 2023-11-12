*** Settings ***
Resource  resource.robot
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
    
*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register
