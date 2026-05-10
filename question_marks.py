"""
https://coderbyte.com/information/Questions%20Marks

Questions Marks

Have the function QuestionsMarks(str) take the str string parameter,
which will contain single digit numbers, letters, and question marks,
and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
If so, then your program should return the string true, otherwise it should return the string false.
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example:
if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3 question marks
 between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.

Examples
Input: "aa6?9"
Output: false
Input: "acc?7??sss?3rr1??????5"
Output: true

References:
https://www.w3schools.com/python/python_dictionaries_loop.asp
"""

def QuestionsMarks(strParam):
    # create a list of dictionaries in the format {index:character}
    characters = []

    for index, char in enumerate(strParam):
        char = {index : char}
        characters.append(char)

    print(characters)

    # filters the characters to just include the index of just the digits
    # I could do this in one step?
    position_of_digits = []

    for index, item in enumerate(characters):
        for key in item:
            if key.isdigit():
                digit = {index : key}
                position_of_digits.append(digit)

    print(position_of_digits)

    # checks if the neighbouring digits sum to 10
    sum_to_10 = []

    for index, item in enumerate(position_of_digits):
        for key in item:

            if index < len(position_of_digits) - 1: # checks if there is another index to check against
                next_item = position_of_digits[index + 1] # gets next item in list

                current_digit = int(list(item.values())[0]) # gets current digit from dict
                next_digit = int(list(next_item.values())[0]) # gets next digit from next item dict

                if current_digit + next_digit == 10: # checks if they sum to 10
                    current_index = list(item.keys())[0] # gets the indices
                    next_index = list(next_item.keys())[0]

                    pairs = (current_index, next_index) # creates indices tuple
                    sum_to_10.append(pairs) # appends to the list

    print(sum_to_10)

    if not sum_to_10: # if nothing was added, strParam has failed
        return "false"

    for start, end in sum_to_10: # uses the indices to slice the string then check for ???
        substring = strParam[start:end]
        if substring.count("?") != 3:
            return "false"

    return "true" # if not false yet, must be true!

print(QuestionsMarks("acc?7??sss?3rr1??????5"))

"""
def QuestionsMarks(string):
    questionMarks = 0
    digits = 0
    total_10 = False 
    for char in string:
        if char.isdigit():#if number
            if int(char) + digits == 10:
                if questionMarks != 3:
                    return 'false'
                total_10 = True
            digits = int(char)
            questionMarks = 0
        elif char == '?':
            questionMarks += 1
    return 'true' if total_10 else 'false'
"""

"""
def QuestionsMarks(s): 
    a, b = 0, 0
    for i in range(len(s)-1):
        for j in range(i, len(s)):
            if s[i].isdigit() and s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
               a, b = i, j
    new = s[a+1:b+1]
    if new.count('?') == 3:
        return 'true'
    else:
        return 'false'
print QuestionsMarks(raw_input())
"""