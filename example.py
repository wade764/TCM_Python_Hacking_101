#!/bin/python3

def test():
    print("Test");

string = "string";
number = 10;

# I can use multiple lines of code in python using the backslash char
x = 1 + 2 \
    + 3

print(x)

print(1+1)
print(__name__)

if __name__ == "__main__":
    print("Do Something");

test()

#help(print)

dir(print)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# The following lines are from the
# Variables and Data Types section of the course
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

name = "Wade"
print(name)

print("The legth of the name string is " + str(len(name)))

name_list = ["Wade", "wadetech.net", "I need a job!"]
print(type(name_list))

name1, name2, name3 = name_list
print(name1)
print(name2)
print(name3)

name_tuple = ("Wade", "another name")
print(type(name_tuple))

name_dictionary = {"Wade": 4, "247CTF": 6}
print(type(name_dictionary))

name_boolean = True
print(type(name_boolean))

name_range = range(6)
print(type(name_range))

name_bytes = b"wade2"
print(type(name_bytes))

print(name_tuple)
print(name_list)
print(name_dictionary)
print(name_boolean)
print(name_range)
print(name_bytes)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
