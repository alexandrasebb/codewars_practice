"""
https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

    Find the unique number (this kata)
    Find the unique string
    Find The Unique
"""
def find_uniq(arr):
    seen_numbers = [] # track the numbers seen so if we get to the end of the sequence and nothing has been return must be the last value in this list

    for i in range(len(arr)):
        num = arr[i] # current number we're interested in

        if num not in seen_numbers: # if it hasn't been seen before append it to seen numbers list
            seen_numbers.append(num)

        if i < (len(arr)-1): # if we aren't at the last item
            next_num = arr[i+1] # get next number

            if num != next_num: # if the current number isn't the same as the next one compare to a third number
                if i == 0: # if we're at the start we can't look at previous number so check against the third ahead
                    if num == arr[i+2]:
                        return next_num # next num must be the odd one out
                    else:
                        return num # num must be odd if it's not equal to either
                if i > 0:
                    prev_num = arr[i - 1]  # get previous number
                    if num == prev_num:
                        return next_num
                    elif num != prev_num:
                        return num

    return seen_numbers[-1]
print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))

"""
def find_uniq(arr):
    # 1. Establish the "Standard" (The common number)
    # We use the first three elements to triangulate.
    a, b, c = arr[0], arr[1], arr[2]
    
    if a == b:
        # A and B are the same, so this is our common value.
        standard = a
    elif a == c:
        # A and C are the same, so A is our common value.
        standard = a
    else:
        # If A matches neither B nor C, B and C MUST be the same.
        # This means A is actually our unique number!
        return a

    # 2. Scan the rest of the "balls" (the array)
    # Now that we know what is 'normal', find the 'odd' one.
    for num in arr:
        if num != standard:
            return num
"""