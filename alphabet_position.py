"""
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
Example

Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

References:
- https://www.geeksforgeeks.org/dsa/ascii-table/
- https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
"""

def alphabet_position(text):
    result = []
    for char in text.lower():
        if char.isalpha() and char.islower():
            code = ord(char) - 96 # - 64 for upper
            result.append(str(code))
        else:
            pass

    result = " ".join(result)
    return result

print(alphabet_position(input()))

"""
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""