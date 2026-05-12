"""
Create a function that validates telephone numbers.
A telephone number is only valid if all validation rules pass.
Return the correct message based on the first rule that fails.

----

Validation Rules

A valid telephone number:

    must contain exactly 11 characters
    must contain digits only
    must start with "07"
    must not contain any spaces
    must not end with "000"
    the sum of all digits must be an even number

If the number passes every rule:
    return "Valid - Even" if the final digit is even
    return "Valid - Odd" if the final digit is odd

----

| Rule Failed                   | Return                    |
| ----------------------------- | ------------------------- |
| Incorrect length              | "Invalid - Length"`     |
| Contains non-digit characters | "Invalid - Digits Only" |
| Invalid prefix                | "Invalid - Prefix"      |
| Contains spaces               | "Invalid - Spaces"      |
| Ends with `"000"`             | "Invalid - Triple Zero" |
| Sum of digits is odd          | "Invalid - Digit Sum"   |

"""
def validate_number(number):
    digits = []

    if len(number) != 11:
        return "Invalid - Length"

    for digit in number:
        if digit not in "0123456789": # if not number.isdigit():
            return "Invalid - Digits Only"
        digits.append(int(digit))

    if not number.startswith("07"):
        return "Invalid - Prefix"

    if " " in number:
        return "Invalid - Spaces"

    if number.endswith("000"):
        return "Invalid - Triple Zero"

    """
    # Rule 6 — Sum of digits must be even
    total = 0

    for digit in number:
        total += int(digit)
    """

    total = sum(digits)

    if total % 2 != 0:
        return "Invalid - Sum"

    if int(number[-1]) % 2 == 0:
        return "Valid - Even"
    else:
        return "Valid - Odd"

# Example tests
print(validate_number("07123456788"))
print(validate_number("07123456781"))
print(validate_number("06123456789"))
print(validate_number("07123abc789"))
print(validate_number("0712345"))
print(validate_number("07123 56789"))
print(validate_number("07123456000"))
print(validate_number("07111111111"))