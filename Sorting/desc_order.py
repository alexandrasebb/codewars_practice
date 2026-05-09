"""
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.
Examples:

Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""

def descending_order(num):
    str_num = list(str(num))
    str_num.sort(reverse=True)
    sorted_num = ''.join(str_num)
    return int(sorted_num)

descending_order(145263)

"""
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def Descending_Order(num):
    return int(''.join(sorted(str(num))[::-1]))
"""