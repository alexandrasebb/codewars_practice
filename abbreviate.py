"""
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""

def abbrev_name(name):
    names = name.split(" ")

    initials = []
    for name in names:
        initials.append(name[0].upper())

    initials = ".".join(initials)
    return initials

print(abbrev_name("Alexandra Sophie Elizabeth Boliver Brown"))

"""
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
"""

"""
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
"""