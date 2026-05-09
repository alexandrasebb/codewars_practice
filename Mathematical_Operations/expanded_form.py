"""
https://www.codewars.com/kata/5842df8ccbd22792a4000245

Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"

NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    digits = list(str(num))[::-1]

    parts = []
    index = 0

    for d in digits:
        if d != '0':
            parts.append(d + ('0' * index))
        index = index + 1
    return " + ".join(parts[::-1])

print(expanded_form(12))