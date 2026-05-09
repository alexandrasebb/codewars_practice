"""
https://www.codewars.com/kata/59df2f8f08c6cec835000012/python

John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

Could you make a program that

    makes this string uppercase
    gives it sorted in alphabetical order by last name.

When the last names are the same, sort them by first name.
Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"

It can happen that in two distinct families with the same family name two people have the same first name too.
Notes

    You can see another examples in the "Sample tests".

    upper_list = map(str.upper, guest_list)
"""

def meeting(s):
    guest_list = s.upper().split(';')
    print(guest_list)

    first_name = []
    last_name = []

    rearranged_names = []

    for guest in guest_list:
        name = guest.split(':')
        last_name.append(name[1])
        first_name.append(name[0])
        joined_names = last_name + first_name
        str_joined_names = ', '.join(joined_names)
        rearranged_names.append(str(str_joined_names))
        first_name.clear()
        last_name.clear()

    sorted_names = []

    for x in sorted(rearranged_names):
        sorted_names.append(f"({x})")

    str_sorted_names = ''.join(sorted_names)

    return str_sorted_names

print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))

"""
def meeting(s):
    names = s.upper().split(";")
    res = []
    for name in names:
        name = name.split(":")
        first, last = name[0], name[1]
        name = (last, first)
        res.append(name)

    res.sort()
    return "".join([f"({last}, {first})" for (last, first) in res]) 
"""

"""
def meeting(s):
    res = []
    names = s.split(";")
    for name in names:
        last_name = name[name.index(":") + 1:]
        first_name = name[:name.index(":")]
        res.append("(" + last_name.upper() + ", " + first_name.upper() + ")")
    res.sort()
    return "".join(res)
"""

"""
def meeting(s):
    return ''.join(sorted('({1}, {0})'.format(*(x.split(':'))) for x in s.upper().split(';')))
"""