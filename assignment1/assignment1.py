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




print (length ("Lucie"))

if startsWith("oliver", "oliv"):
    print("Matched!")
else:
    print("Not matched!")




