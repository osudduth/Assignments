#!/usr/bin/env python3
#
# A game that generates a random number and has the user try and guess it
#
#
# Enhancements: 
#	Instead of printing too high or too low or you guessed it will say them as well1
#	Tells you how many guesses you took3
#	Asks you for your name and addresses you directly7
#	Says top ten high scores6
#	Better error handling of user input2
#	give option to play again5
#	let the user choose the range of numbers the user can guess4
#	

from random import randint 

n = randint(1,100) 
# assigns usernumber to somthing that n cannot be because it needs to be defined but not equal to n before the loop
userNumber = -1
while n != userNumber:
	userNumber = input('Choose a number between 1 and 100: ')
	g = userNumber
	userNumber = int(g)
	if n == userNumber: 
		print ("You guessed it!")
	else:
		if n < userNumber:
			print ("Lower")
		if n > userNumber:
			print ("Higher")
