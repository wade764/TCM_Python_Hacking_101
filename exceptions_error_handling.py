#!/bin/python

print(1)

try:
    f= open("asdasdasdasda")
except:
    print("The file does not exist!")

try:
    f= open("asdasdasdasda")
except Exception as e:
    print(e)

try:
    f= open("asdasdasdasda")
except FileNotFoundError:
    print("The file does not exist!")
except Exception as e:
    print(e)
finally:
    print("This message!")


n = 100
#n = "asd"
if n == 0:
    raise Exception("n can't be 0!")
if type(n) is not int:
    raise Exception("n must be an int")

print(1/n)

#n = 1
n = 0
assert(n != 0)
print(1/n)