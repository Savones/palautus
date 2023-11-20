*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  uusi  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username invalid

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle123  kalle123
    Output Should Contain  Username invalid

Register With Valid Username And Too Short Password
    Input Credentials  kalle  ka12
    Output Should Contain  Password invalid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  maija  kakkeeishifdh
    Output Should Contain  Password invalid

*** Keywords ***
Input New Command And Create User
    Input new Command
    Create User  kalle  kalle123