"""Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel."""

def disemvowel(string_):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    removed_vowels = []
    for letter in string_:
        if letter not in vowels:
            removed_vowels.append(letter)

    str_removed_vowels = ''.join(removed_vowels)

    return str_removed_vowels

print(disemvowel('This website is for losers LOL!'))

"""
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
"""

"""
def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i,'')
    return s
"""

"""
def disemvowel(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:
    	if i not in vowels:
        	new_string+= i 
    return new_string
"""