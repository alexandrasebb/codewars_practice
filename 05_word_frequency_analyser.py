"""
Word Frequency Analyser

Write a function called analyze_text that processes a text string and returns the most frequent word.

Your function should:
1. Take a string parameter (text)
2. Convert the text to lowercase
3. Remove all punctuation marks
4. Split the text into individual words
5. Count the frequency of each word
6. Return the word that appears most frequently


references:
https://realpython.com/sort-python-dictionary/
https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
https://stackoverflow.com/questions/61712565/count-words-in-a-list-and-add-them-to-a-dictionary-along-with-number-of-occurre
https://stackoverflow.com/questions/72899/how-can-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary-in-python
https://stackoverflow.com/questions/30362391/how-to-find-the-first-key-in-a-dictionary-python
"""
import string

def analyze_text(text):
    # Convert the text to lowercase
    text = text.lower()

    # Remove all punctuation marks
    punctuation_removed = ""
    for char in text:
        if char not in string.punctuation:
            punctuation_removed += char

    # Split the text into individual words
    punctuation_removed = punctuation_removed.split(" ")

    # Count the frequency of each word
    words_seen = {}

    for word in punctuation_removed:
        if word not in words_seen:
            words_seen[word] = 1
        else:
            words_seen[word] += 1

    # Sort by frequency to get maximum appearance
    # Sort dictionary by highest frequency
    words_seen = sorted(words_seen.items(), key=lambda item: item[1], reverse=True)
    # print(words_seen)

    # Convert back to a dictionary
    sorted_word_dict = {}
    for key, value in words_seen:
        sorted_word_dict[key] = value
    # print(sorted_word_dict)

    # Find the highest count of words
    highest_count = list(sorted_word_dict.values())[0]
    # print(highest_count)

    # Get the words based on the highest count
    highest_frequency_words = []
    for key, value in sorted_word_dict.items():
        if value == highest_count:
            highest_frequency_words.append(key)

    # print(highest_frequency_words)
    if len(highest_frequency_words) > 1: # # if there's more than 1 word join them with a comma
        highest_frequency_words = ", ".join(highest_frequency_words)
    else:
        return f"The highest frequency words are: {highest_frequency_words[0]}" # if only one return that

    return f"The highest frequency words are: {highest_frequency_words}"

# Test cases
print(analyze_text("The quick brown fox jumps over the lazy dog."))  # "the"
print(analyze_text("Hello world! Hello Python. Python is fun."))  # "hello"
print(analyze_text("a a a b b c"))  # "a"
print(analyze_text("Numbers123 and letters456 should be treated as words."))  # "numbers123"

"""
from collections import Counter
import string
def analyze_text(text):
    # 1
    text = text.lower()
    
    # user tranlators. See link 
    # https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
    
    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator)
    words = text.split()

    frequency = Counter(words)

    return frequency.most_common()[0][0]
"""