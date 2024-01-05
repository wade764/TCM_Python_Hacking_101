#!/bin/python

f = open('top-100.txt')
print(f)

f = open('top-100.txt', 'rt')
print(f)

#print(f.read())

print(f.readlines())
# if you read again without seeking back to the head
# you will just read the end line
f.seek(0)
print(f.readlines())

f.seek(0)
for line in f:
    print(line.strip())

f.close()

# Below is writing to a file
# w is for write mode
# a is for append mode

f = open('test.txt', "a")
f.write("test line!")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

# For larger files it is better to use the file
# object as the iterator, shown below.

with open('rockyou.txt', encoding='latin-1') as f:
    for line in f:
        #print(line)
        pass
