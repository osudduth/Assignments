#!/usr/bin/env python3

#startswith,uppercase,endswith, reverse, ccat

#returns true if word begins with beginning otherwise false

# takes a string and tells you what it starts with
def startsWith(word, beginning):
    for x in range(0, 3):
        if beginning[x] != word[x]:
            return False 

    return True


if startsWith("oliver", "oli"):
    print("Matched!")
else:
    print("Not matched!")