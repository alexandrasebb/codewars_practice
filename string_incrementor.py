"""
https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

https://www.w3schools.com/python/python_regex.asp
https://www.w3schools.com/python/python_strings_methods.asp
https://docs.python.org/3/howto/regex.html
https://docs.python.org/3/library/re.html#re.Pattern.match
https://www.w3schools.com/python/ref_string_zfill.asp
"""
import re

def increment_string(string):
    pattern = re.compile(r"\d+$")
    match = re.search(pattern, string)

    if match:
        x = re.split(pattern, string) # splits the string at the digits
        x = str(x[0])

        num = re.findall(pattern, string)
        num = str(num[0])

        number_length = len(num)
        number = int(num)

        incremented = number + 1
        incremented = str(incremented).zfill(number_length)

        result = x + incremented
    else:
        result = string + "1"
    return result

print(increment_string("foobar0099"))

"""
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
"""

"""
def increment_string(strng):
    
    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')
    
    # get the part of strng that was stripped
    ints = strng[len(stripped):]
    
    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)
    
        # add 1 to ints
        new_ints = 1 + int(ints)
    
        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)
    
        return stripped + new_ints
"""

"""
import re

def increment_string(input):
    match = re.search("(\d*)$", input)
    if match:
        number = match.group(0)
        if number is not "":
            return input[:-len(number)] + str(int(number) + 1).zfill(len(number))
    return input + "1"
"""

"""
import re
def increment_string(strng):
    m = re.match('^(.*?)(\d+)$', strng)
    name, num = (m.group(1), m.group(2)) if m else (strng, '0')
    return '{0}{1:0{2}}'.format(name, int(num)+1, len(num))
"""

"""
def increment_string(s):
    if s and s[-1].isdigit():
        num = s[len(s.rstrip("0123456789")):]
        return s[:-len(num)] + str(int(num) + 1).zfill(len(num))
    
    return s + "1"
"""