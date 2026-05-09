"""
Classwork

# The task:
# Write a function that converts a number into its English word representation.

# Create a function called numberToWords(num) that takes an integer as input
# Break the number into unit groups (ones, tens, hundreds, thousands…)
# Map each digit to its corresponding word (0: "zero", 1: "one", etc.)
# Handle special cases like teens (11–19) which have unique names
# Combine the words in the correct order with appropriate place names
"""

def expanded_form(num):
    digits = list(str(num))[::-1] # turns number into a string, then list and flips the order

    parts = []
    index = 0 # counter for number of zeroes to append

    for d in digits: # as int was turned to str we can iterate
        if d != '0': # checks if the digit is 0 and if not adds it and the number of zeroes appropriate to the place value
            parts.append(d + ('0' * index))
        index = index + 1 # adds one to move to the next place value
    return " + ".join(parts[::-1]) # flips the list back and joins them as a string of numbers separated by +

def num_to_words(num):
    place_values = {2: "hundred",
                    3: "thousand",
                    6: "million",
                    9: "billion",
                    12: "trillion",
                    15: "quadrillion",
                    18: "quintillion",
                    21: "sextillion",
                    24: "septillion"
                    } # powers of 10 in words to the one below 10^26 required by the challenge

    set_numbers = {0: "Zero",
                   1: "One",
                   2: "Two",
                   3: "Three",
                   4: "Four",
                   5: "Five",
                   6: "Six",
                   7: "Seven",
                   8: "Eight",
                   9: "Nine",
                   10: "Ten",
                   11: "Eleven",
                   12: "Twelve",
                   13: "Thirteen",
                   14: "Fourteen",
                   15: "Fifteen",
                   16: "Sixteen",
                   17: "Seventeen",
                   18: "Eighteen",
                   19: "Nineteen",
                   20: "Twenty",
                   30: "Thirty",
                   40: "Forty",
                   50: "Fifty",
                   60: "Sixty",
                   70: "Seventy",
                   80: "Eighty",
                   90: "Ninety"
                   } # specific words for numbers that don't follow the naming pattern

    digits = list(str(num)) # turns input into list to iterate over
    parts = []

    if num in set_numbers: # checks if the number is in the set_numbers dict and if it is returns that
        return f"{set_numbers[num]}"
    else:
        # split the number
        expanded = expanded_form(num) # gets the string from the helper

        # gets the length of original input
        num_length = len(str(num))
        # print(num_length)

        # convert string to int within the list
        expanded = list(map(str, expanded.split(" + "))) # removes + from string
        expanded = list(map(int, expanded))

        if num_length < 4:
            # figure out how to handle each component
            number_string_list = [] # list to put words in

            for component in expanded: # looking at the expanded form parts
                component_str = str(component) # convert to string
                component_len = len(component_str) # get length of string

                if component_len == 3: # hundreds
                    first_digit = int(component_str[0]) # grabs first digit
                    word = f"{set_numbers[int(first_digit)]} {place_values[2]}" # gets the words from the dictionaries
                    number_string_list.append(word) # adds to the list

                elif component_len == 2: # tens logic
                    if component + expanded[-1] in set_numbers: # deals with teens, sort of
                        # going to have to use enumerate:
                        # https://www.geeksforgeeks.org/python/enumerate-in-python/
                        new_number = set_numbers[(component + expanded[-1])]
                        number_string_list.append(new_number)
                        break # don't add the final digit value
                    else:
                        word = set_numbers[component] # gets the component from set values because it's already split!
                        number_string_list.append(word)

                elif component_len == 1:
                    number_string_list.append(set_numbers[component])

            num_string = " ".join(number_string_list).lower() # stitches everything together and lowers for challenge output
            return num_string

print(num_to_words(310))

"""
        for digit in digits:
            parts.append(digit)
            length = len(parts)
            parts.clear()
            expanded = expanded_form(num)
            if length == 2:
                pass
        return
"""

"""
def numberToWords(num):
    ones = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine"}

    teens = {
        10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]

    place = ["", "thousand", "million", "billion", "trillion"]

    chunks = []
    results = []

    while num > 0:
        chunk = num % 1000
        chunks.append(chunk)
        num = num // 1000

    for i in range(len(chunks)):
        chunk = chunks[i]
        words = ""
        if chunk >= 100:
            words += ones[chunk // 100] + " hundred "
            chunk = chunk % 100

        if chunk >= 20:
            words += tens[chunk // 10] + " "
            chunk = chunk % 10
        elif chunk >= 10:
            words += teens[chunk] + " "
            chunk = 0

        if chunk > 0:
            words += ones[chunk] + " "

        if place[i]:
            words += place[i] + " "

        results.append(words)

    results.reverse()
    final = " ".join(results)
    return final.title()


result = numberToWords(12314)
print(result)
"""