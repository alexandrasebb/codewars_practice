"""
https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
 Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 or an empty value like None or null,
depending on your language. You may assume the argument is non-negative.

Examples ( Input --> Output )

121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square

https://www.reddit.com/r/mathematics/comments/1litk2f/the_difference_between_2_sequential_square/
"""

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if sq % sq**(1/2) == 0:
        n = sq**(1/2)
        difference = n + (n + 1)
        return int(sq + difference)
    else:
        return -1

print(find_next_square(81))

"""
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
"""

"""
def find_next_square(sq):
    x = sq**0.5    
    return -1 if x % 1 else (x+1)**2
"""

"""
import math


def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1
"""