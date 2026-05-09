"""
https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indexes of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).

Based on: https://leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)
"""

def two_sum(numbers, target):
    checked_values = {}

    for index, num in enumerate(numbers):
        solution = target - num # calculate the value the answer needs to be

        if solution in checked_values: # if we've already iterated over it, return it
            return (checked_values[solution], index)

        checked_values[num] = index # if not save the current num index to loop again

print(two_sum([1, 2, 3], 4))

"""
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)): # Start 'j' after 'i' so we don't use same index
            if numbers[i] + numbers[j] == target:
                return (i, j)
"""

"""
def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]
"""

"""
def two_sum(numbers, target):
    for i in range(0, len(numbers)):
        for x in range(0, len(numbers)):
            if numbers[i] + numbers[x] == target and i != x:
                index1 = i
                index2 = x
                break
    return sorted([index1, index2])
"""