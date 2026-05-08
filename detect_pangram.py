"""
https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
 because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not.

Ignore numbers and punctuation.
"""

def is_pangram(st):

    letters = []
    for char in st:
        if not char.isalpha():
            pass
        elif char.lower() not in letters:
            letters.append(char.lower())

    if len(letters) == 26:
        return True
    else:
        return False

"""
import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True
"""

"""
import string

def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())
"""