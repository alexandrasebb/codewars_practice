"""
https://www.codewars.com/kata/578553c3a1b8d5c40300037c

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11

However, the arrays can have varying lengths, not just limited to 4.

https://www.w3schools.com/python/ref_func_bin.asp
https://www.sololearn.com/en/compiler-playground/cAI27hk6nVtY/?ref=app
"""

def binary_array_to_number(arr):
    str_num = list(map(str, arr)) # change data types to string
    str_arr = ''.join(str_num) # join the strings together
    arr_int = int(str_arr, 2) # convert binary number to base 2

    return arr_int

print(binary_array_to_number([1,0,1,0]))