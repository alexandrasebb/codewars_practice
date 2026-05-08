"""
https://www.codewars.com/kata/57cff961eca260b71900008f/train/python

Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.
"""

def is_vow(inp):
    # a = 97, e = 101, i = 105, o = 111, u = 117
    codes = [97, 101, 105, 111, 117]
    for char in inp:
        if char in codes:
            position = inp.index(char)
            if char == 97:
                inp[position] = "a"
            elif char == 101:
                inp[position] = "e"
            elif char == 105:
                inp[position] = "i"
            elif char == 111:
                inp[position] = "o"
            elif char == 117:
                inp[position] = "u"
    return inp

print(is_vow([100,100,116,105,117,121]))

"""
def is_vow(inp):
    return [chr(n) if chr(n) in "aeiou" else n for n in inp]
"""

"""
def is_vow(inp):
    for i, v in enumerate(inp):
        if chr(v) in 'aeiou':
            inp[i] = chr(v)
    return inp
"""

"""
def is_vow(s):
    vowels = {97: 'a', 111: 'o', 117: 'u', 101: 'e', 105: 'i'}
    return [vowels.get(a, a) for a in s]
"""