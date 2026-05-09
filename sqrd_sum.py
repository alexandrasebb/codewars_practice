"""
https://www.codewars.com/kata/515e271a311df0350d00000f

Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 1^2+2^2+2^2=9 because 1^2 + 2^2 + 2^2 = 9
"""

def square_sum(numbers):
    total = 0
    for n in numbers:
        total += n ** 2
    return total