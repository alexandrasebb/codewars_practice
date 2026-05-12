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
    # 1. Length: Between 8-30 characters (inclusive)

    if len(password_str) < 8 or len(password_str) > 30:
        return False

    # 2. Uppercase: Contains at least one uppercase letter (A-Z)
    has_one_upper = False
    for char in password_str:
        if char.isupper():
            has_one_upper = True
            break
    if not has_one_upper:
        return False

    # 3. Number: Contains at least one digit (0-9)
    has_one_digit = False
    for char in password_str:
        if char.isdigit():
            has_one_digit = True
            break
    if not has_one_digit:
        return False

    # 4. Punctuation: Contains at least one of these symbols: . , ! ? : ;
    has_one_punctuation = False
    for char in password_str:
        if char in ".,!?;:":
            has_one_punctuation = True
            break
    if not has_one_punctuation:
        return False


    # 5. No "password": Must NOT contain the word "password" (case-insensitive)
    # if password_str.islower() == "password": <- this is wrong
    if "password" in password_str.lower():
        return False

    return True


print(simple_password("apple!M7"))          # → "true"
# simple_password("passWord123!!!!")   # → "false" (contains "password")
# simple_password("turkey90AAA!")      # → "true"
# simple_password("short")             # → "false" (multiple failures)
