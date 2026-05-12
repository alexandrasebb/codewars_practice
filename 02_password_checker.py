"""
Simple Password Validation Challenge

Challenge:
    Write a function simple_password(password_str) that validates if a password
    meets security requirements.

Requirements:
    Your password must satisfy ALL of these conditions:

    1. Length: Between 8-30 characters (inclusive)
    2. Uppercase: Contains at least one uppercase letter (A-Z)
    3. Number: Contains at least one digit (0-9)
    4. Punctuation: Contains at least one of these symbols: . , ! ? : ;
    5. No "password": Must NOT contain the word "password" (case-insensitive)

Return Value:
    - Return "true" if password meets ALL requirements
    - Return "false" if password fails ANY requirement

Examples:
    simple_password("apple!M7")          # → "true"
    simple_password("passWord123!!!!")   # → "false" (contains "password")
    simple_password("turkey90AAA!")      # → "true"
    simple_password("short")             # → "false" (multiple failures)

"""


def simple_password(password_str):
    # Check length is between 8 and 30
    if len(password_str) < 8 or len(password_str) > 30:
        return "False"

    # Check specific requirements
    uppercase_check = []
    digits_check = []
    punctuation_check = []
    for char in password_str:
        # check for upper
        if char.isupper():
            uppercase_check.append(True)
        else:
            uppercase_check.append(False)
        # check for digits
        if char.isdigit():
            digits_check.append(True)
        else:
            digits_check.append(False)
        # check for punctuation
        if char in ".,!?:;":
            punctuation_check.append(True)
        else:
            punctuation_check.append(False)

    if True not in uppercase_check or True not in digits_check or True not in punctuation_check:
        return "False"

    if "password" in password_str.lower():
        return "False"

    return "True"

print(simple_password("A"))          # → "false"
print(simple_password("apPle!m7"))          # → "true"
print(simple_password("passWord123!!!!"))   # → "false" (contains "password")
print(simple_password("turkey90AAA!"))      # → "true"
print(simple_password("short"))             # → "false" (multiple failures)
