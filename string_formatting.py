#!/bin/python3

# Python strings are immutable
# meaning that once that are created
# they can not be changed.
# Python will make copies of the original string.

string1 = "I am a string!"
string2 = 'I am a string too!'

print(string1)
print(string2)

# This is a multiline string
string3 = """I am a long
long
string!"""

print(string3)

# Using an escape sequence
string4 = "I'm a string"
string_test1 = "I\"m a string"
string_test2 = 'I"m a string'

print(string4)

# To search within a string do the following
print("string" in string1)
print("random word" in string1)

# To find the position of a particular word in a string
# do the following
print(string4.index("string"))

print(string1.upper())
print(string1.lower())

messy_string = "   Messy String!   "
print(messy_string)
print(messy_string.strip())

print(messy_string.replace("!","?").strip())

# Making a list with a string
print(messy_string.split())

# You can use split to make a list
# with a delimeter shown below
messy_string2 = "    A messy, messy, weird, string!"
print(messy_string2.split(","))

string5 = "This is an example of adjusting encoding!"
print(string5)
print(string5.encode())
print(string5.encode("utf-8"))

print(string4.rjust(25))
print(string4.rjust(25), "X")
