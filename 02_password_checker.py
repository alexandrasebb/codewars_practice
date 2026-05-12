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
    pass



# print(simple_password("A"))          # → "false"
# print(simple_password("apPle!m7"))          # → "true"
# simple_password("passWord123!!!!")   # → "false" (contains "password")
# simple_password("turkey90AAA!")      # → "true"
# simple_password("short")             # → "false" (multiple failures)
