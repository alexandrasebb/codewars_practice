"""
Write a function to split a string and convert it into an array of words.
"""

def string_to_array(s):
    if s is "":
        return [""]
    return s.split()
