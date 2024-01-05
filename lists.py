#!/bin/python3

list1 = ["A", "B", "C", "D", "E", "F"]
print(list1)

list2 = ["A", 1, 2.0, ["A"], [], list(), ("A"), False]
print(list2)
print(type(list2))

# You can replace an item with a list like this
list1[0] = "X"
print(list1)

# You can delete an item at a particular index
del list1[0]
print(list1)

# You can add an item at a specific index
list1.insert(0, "A")
print(list1)

del list1[0]
print(list1)

list1 = ["A"] + list1
print(list1)

list1.append("G")
print(list1)

# The largest value in the list
print(max(list1))

# The smallest value in the list
print(min(list1))

# The index of C
print(list1.index("C"))

# The value located at the index of C
print(list1[list1.index("C")])

# One way to reverse a list
# ***NOTE*** Once a list is reversed is stays that way
# To return the list to its original state
# Perform a second reverse operation
#list1.reverse()
#print(list1)

# Syntactic suger for reversing a list
list1 = list1[::-1]
print(list1)

# The number of times A appears in the list
print(list1.count("A"))
# Adding another A
list1.append("A")
print(list1)
print(list1.count("A"))

# You can pop items from a list
list1.pop()
print(list1)

list3 = ["H", "I", "J"]
print(list3)

list1.extend(list3)
print(list1)

list1.clear()
print(list1)

list4 = [8, 12, 5, 6, 17, 2]
print(list4)

list4.sort()
print(list4)

list4.sort(reverse=True)
print(list4)

list5 = list4
print(list4)
print(list5)

# If you set one list to another you
# are just shifting pointers so any changes you make
# will change the original referenced datastructure
list5[2] = "X"
print(list5)
print(list4)

# To avoid overwriting the original DS
# You need to make a copy of it like this
list6 = list4.copy()
print(list4)
print(list6)

list6[2] = "A"
print(list4)
print(list6)

# The map function is used to apply some
# function to every item in the list
list7 = ["1", "2", "3"]
print(list7)

# I am casting each item as a float
# and adding it to a new list
list8 = list(map(float, list7))
print(list8)
print(list7)




