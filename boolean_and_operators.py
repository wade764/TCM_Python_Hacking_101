#!/bin/python3

valid = True
notValid = False

print(valid)
print(notValid)

print(valid == True)
print(notValid == False)

# He covered a lot of arithmetic operations
# and more variable assignment stuff.

# This course is very basic so far
# but a good refresher

# The [2:] will remove the first leading chars 0b
x = 13
#print("x = " + bin(x))
print("This is a bitwise AND operation")
print("x = " + bin(x)[2:].rjust(4,"0"))

y = 5
print("y = " + bin(y)[2:].rjust(4,"0"))

# bitwise and operation
print("    " + bin(x & y)[2:].rjust(4, "0"))

print("    " + str(x & y))

# bitwise or operation
print("This is a bitwise OR operation")
print("x = " + str(bin(x)[2:].rjust(4,"0")))
print("y = " + str(bin(y)[2:].rjust(4,"0")))

print("    " + str(bin(x | y)[2:].rjust(4, "0")))

print("    " + str(x | y))

# bitshifting
print("x = " + str(x))
print("binary x = " + str(bin(x)[2:].rjust(8,"0")))
print("Performing a 2 left bitshift operation on x below.")
print(bin(x << 2)[2:].rjust(8, "0"))
