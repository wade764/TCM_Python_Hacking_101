#!/bin/python

# This covers list comprehensions.
# Comprehensions provide a shorter syntax
# to create a list based on some iterable


list1 = ['a', 'b', 'c']
print(list1)

# This is a comprehension
list2 = [x for x in list1]
print(list2)

list3 = [x for x in list1 if x == 'a']
print(list3)

list4 = [x for x in range(5)]
print(list4)

list5 = [hex(x) for x in range(5)]
print(list5)

list6 = [hex(x) if x > 0 else "X" for x in range(5)]
print(list6)

list7 = [x * x for x in range(5)]
print(list7)

list8 = [x for x in range(5) if x == 0 or x == 1]
print(list8)

list9 = [[1,2,3],[4,5,6],[7,8,9]]
print(list9)

list10 = [y for x in list9 for y in x]
print(list10)

# comprehensions can be used on sets as well as lists
set1 = {x + x for x in range(5)}
print(set1)

list11 = [c for c in "string"]
print(list11)

# join can be used in a comprehension to combine items
# in an iterable into a single string
print("".join(list11))

print("-".join(list11))

# comprehensions are just a shorthand and
# you can create the same output using long form
# as shown below
list12 = []
for c in "string":
    list12.append(c)
print(list12)

