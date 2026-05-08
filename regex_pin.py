"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""

import re

def validate_pin(pin):
    var = len(pin)

    if var == 4 or var == 6:
        match = re.match("^(\d{4}|\d{6})$", pin)

        if not match:
            return False
        else:
            return True
    else:
        return False

validate_pin('09876\n')

"""
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
"""

"""
def validate_pin(pin):
    #return true or false
    return bool(re.fullmatch("\d{4}|\d{6}", pin))
"""