"""
This time no story, no theory. The examples below show you how to write function accum:
Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z."""

def accum(st):
    st_list = list(st.upper())
    count = 0
    mumbled = []

    for item in st_list:
        mumbled.append(item + (item.lower()*count))
        count = count + 1
    return "-".join(mumbled)

print(accum("abcd"))