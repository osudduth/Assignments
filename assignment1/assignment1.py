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
   if length(word) < length (subWord):
       return False

   for y in range (0, length(word)):
        w =  word[y:]
        if startsWith (w, subWord):
            return True
   return False    


#
#In this function you will give it a string and it will reverse the order of the letters in the string
#


def mirror(word):
    x = length(word) - 1
    mirrorWord = [None] * length(word)
    for l in word:
        mirrorWord[x] = l  
        x = x - 1
    return  ''.join(mirrorWord)


#
#This function will take in a word and then a subword and it will see if the word ends with the subword
#


def endsWith(word, subword):
    mirror(word)
    mirror(subword)
    if startsWith(mirror(word), mirror(subword)):
        return True
    else:
        return False


            
    
if contains("wordword", "poop"):
    print("failed")
else:
    print("passed")

if contains("wordword", "rdw"):
    print ("passed")
else:
    print("failed")

if startsWith("oliver", "oliv"):
    print("passed")
else:
    print("failed")

if contains ("oli", "oliver"):
    print ("failed")
else:
    print ("passed")

if (contains("zza", "azza")):
    print("failed")
else:
    print("passed")




if "eyb" == mirror("bye"):
    print("passed")
else:
    print("failed")


if endsWith ("birthday", "day"):
    print ("passed")
else:
    print ("failed")


if endsWith ("birthday", "dag"):
    print ("passed")
else:
    print ("failed")








