"""
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    count = 0

    for char in sentence:
        if char in "aeiou":
            count += 1
        else:
            pass
    return count

print(get_count("abracadabra"))

"""
def getCount(s):
    return sum(c in 'aeiou' for c in s)
"""

"""
import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))
"""

"""
def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])
"""