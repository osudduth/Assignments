#!/usr/bin/env python3
#
# A game that generates a random number and has the user try and guess it
#
#
# Enhancements: 
#	Instead of printing too high or too low or you guessed it will say them as well1
#	Asks you for your name and addresses you directly7
#	Says top ten high scores6
#	Better error handling of user input2
#	give option to play again5
#	let the user choose the range of numbers the user can guess4
#	

from random import randint
def playgame(): 
	guess = 0
	n = randint(1,100) 
	# assigns usernumber to somthing that n cannot be because it needs to be defined but not equal to n before the loop
	userNumber = -1
	
	while n != userNumber:
		guess = guess + 1
		userNumber = input('Choose a number between 1 and 100: ')
		g = userNumber
		userNumber = int(g)
		if n == userNumber: 
			print ("You guessed it in " + str(guess) + " guesses!")
		else:
			if n < userNumber:
				print ("Lower")
			if n > userNumber:
				print ("Higher")
	
#
#make the gane into a function and then run a loop around the function that asks if you want to play again
#	
cont= True
while cont:
	playgame()
	answer = input('Press y to play again. Press any other letter to quit: ')
	if answer != "y":
		cont =  False

print ("\nGood Riddance!\n")		 	 
