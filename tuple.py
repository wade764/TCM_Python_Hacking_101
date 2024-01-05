#!/bin/python3

tuple_items = ("item1", "item2", "item3")
print(tuple_items)
print(type(tuple_items))

tuple_numbers = (1, 2, 3)
print(tuple_numbers)
print(type(tuple_numbers))

tuple_repeat = ('Combine!',) * 4
print(tuple_repeat)
print(type(tuple_repeat))

# You can create a tuple with mixed variable types
mixed_tuple = ("A", 1, ("A", 1))
print(mixed_tuple)
print(type(mixed_tuple))

# Because variables in Python are immutable
# You can not append() an item to a tuple
# You can however do the following.
tuple_combined = tuple_items + tuple_numbers
print(tuple_combined)
print(type(tuple_combined))

item1, item2, item3 = tuple_items
print(item1)
print(item2)
print(item3)

print("item2" in tuple_items)
print("item3" in tuple_items)
print("item4" in tuple_items)

print(tuple_items.index("item2"))

tuple_items = ("item1", "item2", "item3")
print(tuple_items[0])
print(tuple_items[1])
print(tuple_items[2])

# This will print out the last item in the tuple
print(tuple_items[-1])
# This will print out the next to last item in the tuple
print(tuple_items[-2])

print(tuple_items[0:2])
print(tuple_items[:2])
print(tuple_items[-3:-1])

string1 = "I am a string!"
# This will print the last char in the string
print(string1[-1])
# This will print everything up to the last char in the string
print(string1[:-1])