"""
https://www.codewars.com/kata/546e2562b03326a88e000020

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!
"""

def square_digits(num):
    digits = list(str(num))
    int_num = list(map(int, digits))

    sqrd = []
    for n in int_num:
        sqrd.append(n ** 2)

    sqrd_str = list(map(str, sqrd))
    outcome = "".join(sqrd_str)
    return int(outcome)

print(square_digits(12345))

"""
def square_digits(num):
    # 1. Loop through each character in the string of num
    # 2. Square it
    # 3. Join them all together
    # 4. Cast back to int
    return int("".join(str(int(d)**2) for d in str(num)))
    
def square_digits(num):
    squares = '' # Empty string
    for x in str(num):
        squares += str(int(x) ** 2)
    return int(squares)
"""
