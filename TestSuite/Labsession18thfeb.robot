*** Settings ***
Library    Collections


*** Variables ***
${NAME}        Manivas
${NUM1}        10
${NUM2}        20
${CITY}        Hyderabad

@{FRUITS}      apple    banana    mango

&{USER}        username=admin    password=admin123


*** Test Cases ***
Variables Practice

    # 1️⃣ Print scalar variable
    Log To Console    ${NAME}

    # 2️⃣ Print sum of two numbers
    ${sum}=    Evaluate    ${NUM1} + ${NUM2}
    Log To Console    Sum is: ${sum}

    # 3️⃣ Use variable inside sentence
    Log To Console    I live in ${CITY}

    # 4️⃣ Reassign variable inside test case
    ${CITY}=    Set Variable    Chennai
    Log To Console    Updated city: ${CITY}

    # 5️⃣ Print first item of list
    Log To Console    First fruit: ${FRUITS}[0]

    # 6️⃣ Loop through list
    FOR    ${item}    IN    @{FRUITS}
        Log To Console    ${item}
    END

    # 7️⃣ Find length of list
    ${length}=    Get Length    ${FRUITS}
    Log To Console    Length of list: ${length}

    # 8️⃣ Print dictionary key value
    Log To Console    Username: ${USER}[username]

    # 9️⃣ Add new key-value pair to dictionary
    Set To Dictionary    ${USER}    email=admin@gmail.com
    Log To Console    Email: ${USER}[email]

