"""
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
"""

def reverse_seq(n):
    nums = []
    nums.append(n)
    while nums[-1] != 1:
        n = n - 1
        nums.append(n)
    return nums

print(reverse_seq(5))

"""
def reverseseq(n):
    return list(range(n, 0, -1))
"""