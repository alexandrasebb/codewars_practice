"""
https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"
"""

def spin_words(sentence):
    words = sentence.split(" ")
    output = []
    for word in words:
        if len(word) >= 5:
            reversed = word[::-1]
            output.append(reversed)
        else:
            output.append(word)
    result = " ".join(output)
    return result

print(spin_words("Just with word of words included"))

"""
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
"""

"""
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)
"""