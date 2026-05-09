"""
https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized, and remaining letters lowercased.

    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s):
    s = " ".join(s.split()) # removes whitespace between words and leaves a single space between
    # https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string

    if len(s) == 0:
        return False

    s = s.split(" ") # split the word at the remaining space
    processed = ["#"] # start the list with the hashtag instead of appending it

    for word in s: # for each word in the input
        # word = word.strip() # dealt with this in the first line
        processed_word = []
        position = 0
        for char in word: # using index [0] was appending all upper so used count instead
            position += 1
            if position == 1:
                processed_word.append(char.upper()) # capitalise the first letter and append
            else:
                processed_word.append(char.lower())
        processed.append("".join(processed_word)) # join the items in processed word and append that to the general processed
    result = "".join(processed) # join processed list into a string
    result.replace(" ", "") # remove spaces

    if len(result) > 140: # check result for length
        return False

    return result

print(generate_hashtag("    Hello     World   "))

"""
def generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
"""

"""
def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False
"""

"""
def generate_hashtag(s):
    s = s.split()
    if len(s) > 140 or not (s):
        return False
    ans = '#'
    for word in s:
        ans += word.title()
    if len(ans) > 140 or not (s):
        return False
    return ans
"""

"""
def generate_hashtag(s):
    return s if s and len(s := "#" + s.title().replace(" ", "")) <= 140 else False
"""