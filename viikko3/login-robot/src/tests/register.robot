*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials    tunnus    sala!sana
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    [Setup]    Input New Command And Create User
    Input New Command
    Input Credentials    kalle    kalle123
    Output Should Contain    Username already taken

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials    tu    sala!sana
    Output Should Contain    Invalid username

Register With Enough Long But Invald Username And Valid Password
    Input New Command
    Input Credentials    tunnus#    sala!sana
    Output Should Contain    Invalid username

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials    tunnus    sala!sa
    Output Should Contain    Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials    tunnus    salasana
    Output Should Contain    Invalid password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials    kalle    kalle123