"""
Classwork
https://www.codewars.com/kata/53c94a82689f84c2dd00007d

# The task:
# Write a function that converts a number into its English word representation.

# Create a function called numberToWords(n) that takes an integer as input
# Break the number into unit groups (ones, tens, hundreds, thousands…)
# Map each digit to its corresponding word (0: "zero", 1: "one", etc.)
# Handle special cases like teens (11–19) which have unique names
# Combine the words in the correct order with appropriate place names
"""
def expanded_form(n):
    digits = list(str(n))[::-1] # turns number into a string, then list and flips the order

    parts = []
    index = 0 # counter for number of zeroes to append

    for d in digits: # as int was turned to str we can iterate
        if d != '0': # checks if the digit is 0 and if not adds it and the number of zeroes appropriate to the place value
            parts.append(d + ('0' * index))
        index = index + 1 # adds one to move to the next place value
    return parts[::-1] # flips the list back

def three_digits_to_words(n, ones, teens, tens, place_values):
    pass

def int_to_english(n):
    place_values = {2: "hundred",
                    3: "thousand",
                    6: "million",
                    9: "billion",
                    12: "trillion",
                    15: "quadrillion",
                    18: "quintillion",
                    21: "sextillion",
                    24: "septillion"} # powers of 10 in words to the one below 10^26 required by the challenge

    ones = {0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine"} # names of individual digits

    teens = {11: "eleven",
             12: "twelve",
             13: "thirteen",
             14: "fourteen",
             15: "fifteen",
             16: "sixteen",
             17: "seventeen",
             18: "eighteen",
             19: "nineteen"} # names of two digit numbers not 10

    tens = {10: "ten",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety"} # names of ten values

    if n in ones or n in teens or n in tens: # checks if the number is in any of the dicts and if it is returns that
        if n in ones:
            return ones[n]
        if n in teens:
            return teens[n]
        if n in tens:
            return tens[n]
    else:
        # split the number
        expanded = expanded_form(n) # gets the string from the helper

        # gets the length of original input
        num_length = len(str(n))
        # TODO: use num length to chop up numbers into three digit parts
        # print(num_length)

        # convert string to int within the list
        expanded = list(map(int, expanded))

        if n < 1000:
            three_digits_to_words(expanded, ones, teens, tens, place_values)

            # TODO: move this to it's own function, call on each chunk

            number_string_list = [] # list to put words in

            for component in expanded: # looking at the expanded form parts
                component_str = str(component) # convert to string
                component_len = len(component_str) # get length of string

                if component_len == 3: # hundreds
                    first_digit = component_str[0] # grabs first digit
                    word = f"{ones[int(first_digit)]} {place_values[2]}" # gets the words from the dictionaries
                    number_string_list.append(word) # adds to the list

                elif component_len == 2: # tens logic
                    if component == 10 and len(expanded) > 1 and component + expanded[-1] in teens: # deals with teens
                        new_number = teens[(component + expanded[-1])]
                        number_string_list.append(new_number)
                        break # don't add the final digit value
                    elif component in tens:
                        number_string_list.append(tens[component])

                elif component_len == 1:
                    number_string_list.append(ones[component])

            num_string = " ".join(number_string_list).lower() # stitches everything together and lowers for challenge output
        return num_string

print(int_to_english(550))

"""
def numberToWords(n):
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

    while n > 0:
        chunk = n % 1000
        chunks.append(chunk)
        n = n // 1000

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