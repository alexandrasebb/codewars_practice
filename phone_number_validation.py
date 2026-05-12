"""
Phone Number Validator

Write a function called validate_phone that checks if a string is a valid phone number
according to the following rules:

1. The phone number must be in the format: XXX-XXX-XXXX (3 digits, hyphen, 3 digits, hyphen, 4 digits)
2. All characters except hyphens must be digits
3. The first digit cannot be 0 or 1 (US area codes don't start with these)
4. The first three digits (area code) cannot be 911
5. The middle three digits cannot be all the same digit (e.g., 555)

Your function should return True if all conditions are met, and False otherwise.
"""

def validate_phone(phone_number):

    if len(phone_number) != 12:
        return False

    for index, digit in enumerate(phone_number):
        if index == 3 or index == 7:
            if digit not in "-":
                return False
        elif not digit.isdigit():
            return False
        else:
            pass

    middle_digit = []
    for index, digit in enumerate(phone_number):
        if index < 4 or index > 6:
            pass
        else:
            middle_digit.append(int(digit))

    if middle_digit[0] == middle_digit[1] == middle_digit[2]:
        return False

    # sum_middle_digits = sum(middle_digit)
    # if sum_middle_digits // middle_digit[0] == middle_digit[0]:
    #     return False

    if phone_number.startswith("911") or phone_number.startswith("1") or phone_number.startswith("0"):
        return False
    else:
        return True

# Test cases
print(validate_phone("212-4567890"))  # False (wrong format)
print(validate_phone("123-456-7890"))  # False (area code starts with 1)
print(validate_phone("911-456-7890"))  # False (area code is 911)
print(validate_phone("212-555-3456"))  # False (middle section has all same digits)
print(validate_phone("212-456-7890"))  # True

"""
def validate_phone(phone_number):
    # Section 1
    parts = phone_number.split("-")
    # print("Parts", parts)
    if len(parts[0]) != 3:
        return False
    if len(parts[1]) != 3:
        return False
    if len(parts[2]) != 4:
        return False

    # Section 2
    if not parts[0].isdigit():
        return False
    if not parts[1].isdigit():
        return False
    if not parts[2].isdigit():
        return False

    # Section 3
    if parts[0][0] == "1":
        return False
    if parts[0][0] == "0":
        return False

    # Section 4
    if parts[0] == "911":
        return False

    # Section 5
    if parts[1][0] == parts[1][1] == parts[1][2]:
        return False

    # all checked passed - ALL GOOD
    return True
"""