#!/bin/python

test = input()
print(test)

test = input("Enter the IP: ")
print(test)

while True:
    test = input("Enter the IP: ")
    print(">>> {}".format(test))
    if test == "exit":
        break
    else:
        print("exploiting..")
