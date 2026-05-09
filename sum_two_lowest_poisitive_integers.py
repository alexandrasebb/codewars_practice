"""
https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers.
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.
"""

def sum_two_smallest_numbers(numbers):
    lowest_number = []
    for number in numbers:
        if len(lowest_number) == 0:
            lowest_number.append(number)
        elif number < lowest_number[-1]:
            lowest_number.pop()
            lowest_number.append(number)
    numbers.remove(lowest_number[0])

    for number in numbers:
        if len(lowest_number) == 1:
            lowest_number.append(number)
        elif number < lowest_number[-1]:
            lowest_number.pop()
            lowest_number.append(number)

    return sum(lowest_number)

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

"""
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""

"""
def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]
"""

"""
def sum_two_smallest_numbers(numbers):
    smallest1 = None
    smallest2 = None 
    for n in numbers: 
        if not smallest1 or n < smallest1: 
            smallest2 = smallest1
            smallest1 = n 
        elif not smallest2 or n < smallest2: 
            smallest2 = n 
    return smallest1 + smallest2
"""