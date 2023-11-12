*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  pelle  hermann1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  kalle  kalle1234
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  pe  hermann1
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invald Username And Valid Password
    Input New Command
    Input Credentials  pell3  hermann1
    Output Should Contain  Username can only contain letters from a-z

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  pelle  herman1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  pelle  hermanni
    Output Should Contain  Password must contain non-letter characters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  kalle  kalle1234