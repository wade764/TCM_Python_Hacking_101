#!/bin/python

def function1():
    print("hello from function1!")

function1()
function1()

def function2():
    return "Hello from function2!"

print(function2())

def function3(s):
    print("\t{}".format(s))

function3("parameter")

def function4(s1, s2):
    print("{} {}".format(s1,s2))

function4("any","thing")
function4(s2="any", s1="thing")

def function5(s1 = "default"):
    print("{}".format(s1))

function5()
function5("anything")

def function6(s1, *more):
    print("{} {}".format(s1, " ".join([s for s in more])))

function6("function6")
function6("function6", str([x for x in range(5)]))

# This is using a dictionary as an argument
def function7(**ks):
    for a in ks:
        print(a, ks[a])

function7(a="1", b="2", c="3")

def function8(s, f, i, l):
    print(type(s))
    print(type(f))
    print(type(i))
    print(type(l))

function8("string", 1.0, 1, ['l', 'i', 's', 't'])

v = 100
print(v)

def function9():
    global v
    v += 5
    print(v)

function9()
print(v)

def function10():
    print("hello from function10!")

def function11():
    print("hello from function11!")
    function10()

function11()

# This is an example of recursion
def function12(x):
    print(x)
    if x > 0:
        function12(x - 1)

function12(5)

