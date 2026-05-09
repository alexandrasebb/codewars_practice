"""
https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""

def reverse_words(text):
    text_list = list(text.split(' ')) # preserves original spacing if there are double spaces
    reversed_list = []
    for word in text_list:
        reversed_list.append(word[::-1])
    return ' '.join(reversed_list)

print(reverse_words('This is an example!'))

"""
def reverse_words(text):
    return ' '.join(word[::-1] for word in text.split(' '))
"""