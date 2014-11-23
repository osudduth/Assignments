#!/usr/bin/env python3

#startswith,uppercase,endswith, reverse, ccat

#
# this will tell you the length of the given string 
#
def length(word): #defined function and arguments
    z = 0 #defined counter
    for l in word: #defined a loop that stores each letter of the word in l
        z = z + 1 #making the counter go up by one
    return z #told it what to return

#
# returns true if word begins with beginning otherwise false
#
def startsWith(word, beginning):# defined function and arguments
    for x in range(0, length(beginning) ):#defined loop that goes from 0 to the length of the word that we are testing
        if beginning[x] != word[x]:#compared the letter that x is on in word and beginning then if  not equal return false 
            return False #return false
    return True #if all the letters are equal return true

#
# This will return true if a string contains another smaller string and false if it doesnt
#
def contains(word, subWord):#defined function and arguments
   if length(word) < length (subWord):#if the length of the word is less than that of the subword return false
       return False

   for y in range (0, length(word)):#defining loop that says start at zero and go untill the end of the length of word
        w =  word[y:]#defining w initializes it to  all of the letters in the word
        if startsWith (w, subWord):#this compares if word starts with the subword
            return True #this says return true if it does contain 
   return False    #this says that if the word does not contain the subword return false


#
#In this function you will give it a string and it will reverse the order of the letters in the string
#


def mirror(word):#defining arguments and function
    x = length(word) - 1 #defining counter that is the length of the word minus 1
    mirrorWord = [None] * length(word)#making an array that is the exact space of the word
    for l in word:#making a loop that runs through all the letters
        mirrorWord[x] = l  #storing the letter in mirrorWord at x
        x = x - 1#starting the loop that goes down 1
    return  ''.join(mirrorWord)#turning the mirrorword array into a string


#
#This function will take in a word and then a subword and it will see if the word ends with the subword
#


def endsWith(word, subword):#defining the function and arguments
    if startsWith(mirror(word), mirror(subword)):#here it is saying if the mirrored word starts with the mirrored subword return true if not return false
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








