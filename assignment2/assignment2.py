#!/usr/bin/env python3

#startswith,uppercase,endswith, reverse, ccat

#
# this will tell you the length of the given string 
#
def length(word): #defined function and arguments
    z = 0 #defined counter
    for l in word: #defined type of loop
        z = z + 1 #told the loop how to run
    return z #told it what to return

#
# returns true if word begins with beginning otherwise false
#
def startsWith(word, beginning):# defined function and arguments
    for x in range(0, length(beginning) ):#defined loop
        if beginning[x] != word[x]:#told the compiler that if the beginning word was not equal to the regular word
            return False #return false
    return True #but if it does equal the beginning return true

#
# This will return true if a string contains another smaller string and false if it doesnt
#
def contains(word, subWord):#defined function and arguments
   if length(word) < length (subWord):#if the length of the word is less than that of the subword return false
       return False

   for y in range (0, length(word)):#defining loop
        w =  word[y:]#defining counter
        if startsWith (w, subWord):#this says that if word contains subword return true if not return false
            return True
   return False    


#
#In this function you will give it a string and it will reverse the order of the letters in the string
#


def mirror(word):#defining arguments and function
    x = length(word) - 1 #defining counter
    mirrorWord = [None] * length(word)#i dunno
    for l in word:#defining loop
        mirrorWord[x] = l  #i dunno
        x = x - 1#starting the loop
    return  ''.join(mirrorWord)#i dont know


#
#This function will take in a word and then a subword and it will see if the word ends with the subword
#


def endsWith(word, subword):#defining the function and arguments
    mirror(word)# telling the compiler to turn the word backewards by calling in the mirror word function
    mirror(subword)#here it is telling the compiler to reverse the subword by calling the mirrror word iagain on the subword
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








