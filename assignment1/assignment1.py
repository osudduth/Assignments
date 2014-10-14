#!/usr/bin/env python3

#startswith,uppercase,endswith, reverse, ccat

#
# this will tell you the length of the given string 
#
def length(word):
    z = 0
    for l in word:
        z = z + 1 
    return z

#
# returns true if word begins with beginning otherwise false
#
def startsWith(word, beginning):
    for x in range(0, length(beginning) ):
        if beginning[x] != word[x]:
            return False 
    return True

#
# This will return true if a string contains another smaller string and false if it doesnt
#

def contains(word, subWord):
    for y in range (0, length(word)):
        print (word[y:])

    return True


if contains("wordword", "rdw"):
    print("does contain")
else:
    print("does not contain")



if contains("wordword", "oliver"):
    print("does contain")
else:
    print("does not contain")

print (length ("Lucie"))

if startsWith("oliver", "oliv"):
    print("Matched!")
else:
    print("Not matched!")

