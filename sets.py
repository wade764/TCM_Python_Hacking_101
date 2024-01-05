#!/bin/python3

# A set is similar to a dictionary
# but there is no key value pair assigned

set1 = {"a", "b", "c"}
print(set1)
print(type(set1))

# Sets are not ordered so when you print them
# they will be printed in a random order every
# time the program is executed

set2 = {"a", "a", "a"}
print(set2)
print(type(set2))

set3 = {"a", 0, True}
print(set3)

set4 = set(("b", 1, False))
print(set4)

set1.add("d")
print(set1)

set3.update(set4)
print(set3)

# Sets can not contain multiple values

list1 = ["a", "b", "c"]
set4 = {4, 5, 6}
print(list1)
print(set4)

set4.update(list1)
print(set4)

# Sets are Mathmatical constructs

set5 = {4, 5, 6}
set6 = set4.union(set4)
print(set6)

set4.remove(4)
print(set4)

# remove only works for items that are already in the set
# If instead you want to remove
# an item regardless if it is in a set or not
# you can use the discard() function

set4.discard(4)
print(set4)

# You can use pop() but because
# Sets are not ordered you only want to use
# pop() when you do not care what is being
# removed.

print(set1)
set1.pop()
print(set1)

# Sets are good to use when you do not care
# about the order and you do not want duplicates
