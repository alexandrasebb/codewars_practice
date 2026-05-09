"""
https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python


Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

def pig_it(text):
    words = list(text.split(" "))
    pig = []
    suffix = "ay"

    for word in words:
        if not word.isalpha():
            pig.append(word)
        else:
            position = 0
            current_word = []
            for char in word:
                position += 1
                if not char.isalpha():
                    current_word.append(char)
                elif position == 1:
                    starting_letter = char
                else:
                    current_word.append(char)
            current_word.append(starting_letter)
            current_word = "".join(current_word)
            pig.append(f"{current_word}{suffix}")
    return " ".join(map(str, pig))

print(pig_it("Hello world !"))
