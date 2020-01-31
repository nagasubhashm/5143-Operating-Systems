"""
A bunch of random code snippets as an intro to python
"""

import pprint   # prints things out with nice indentation

from process_text import readFile       # example imports of own methods
from process_text import countWords
from process_text import TextProcessing

tp = TextProcessing("text.txt")         # create instance of a class
data = tp.readFile()                    # call classes methods
words = tp.countWords(data)

print(words)                            # print words to output

A = []                  # create an empty list

A.append(34)            # append different kinds of data to the list
A.append(234)
A.append("hello")
A.append("sue")
A.append([1, 2, 3, 4])

print(type(A))          # type function gives the 'type' of an object         
print(A)                # print the list to output

for a in A:             # looping through a list
    print(a)

for i in range(len(A)): # different way to loop through a list
print(A[i])

D = {}                  # create a dictionary

D['apple'] = 4          # put random stuff in dictionary
D['banana'] = 5
D['peach'] = 7
D[9] = 'banana'
D[0] = A

if 'apple' in D:        # wrong way to loop through dictionary
    print("key apple is in D")

pprint.pprint(D)        # pretty print the dictionary

print(D[0][1])          # print 1st item in a list at key[0]

point = (3, 4, 5)       # tuple data type (immutable)

print(point[0])         # access tuples data
print(point[1])

x, y, z = point         # tuple with 3 items will put each item
                        # in x,y,z (easy way to pull data out)

print(x)                # showing that the assignment worked
print(y)
print(z)

for k, v in D.items():  # proper way to loop through dictionary
    print(k, v)

if "sue" in A:          # test if value in list A
    print("value exists")

print(D.values())       # print all the values in the dictionary 
                        # NOT the keys

print(D.keys())         # this prints JUST the keys

# random string to show how "in" works
s = "a;sdlkfja;sldkfuasdfaj;sldkfjqaweiurknaiuasdhfinbasdiuofa"

# this evaluates to true since "uas" is a substring of 's'
if "uas" in s:
    print("hello world!!!!!!!")

x = 100                 # var is an int

x = [1, 2, 3]           # var is now a list

x = {"hello": "world"}  # var is now a dictionary

# prints out the makeup (directory) of the TextProcessing class definition
print(dir(TextProcessing))

# prints the contents of the instance of the TextProcessing class
print(tp)