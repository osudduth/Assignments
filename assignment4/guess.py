#!/usr/bin/env python3
#
# A game that generates a random number and has the user try and guess it
#
#
# Enhancements:
#	Instead of printing too high or too low or you guessed it will say them as well1
#	better user error handling
#
from random import randint
import sys

#
#asks the user for a number and handles bad input
#
def inputInteger(prompt):
	while True:
		try:
			userNumber = int(input(prompt))
			break
		except ValueError:
			print("\nOops!  That was no valid number.  Try again...\n")

	return userNumber
	

def playgame(upperBoundary):
	guess = 0
	n = randint(1, upperBoundary)
	# assigns usernumber to somthing that n cannot be because it needs to be defined but not equal to n before the loop
	userNumber = -1

	while n != userNumber:
		guess = guess + 1
		userNumber = inputInteger('\nChoose a number between 1 and ' + str(upperBoundary) +', ' + name + ': ')
		g = userNumber
		userNumber = int(g)
		if n == userNumber:
			print ("\nNice job " + name + "! You guessed it in " + str(guess) + " guesses!\n")
		else:
			if n < userNumber:
				print ("Lower")
			if n > userNumber:
				print ("Higher")

#
#make the gane into a function and then run a loop around the function that asks if you want to play again
#
cont= True
name = input('What is your name?: ')
while cont:
	upperBoundary = inputInteger("\nWhat is the highest number you want to guess to?  ")
	playgame(int(upperBoundary))
	answer = input('Press y to play again. Press any other letter to quit: ')
	if answer != "y":
		cont =  False

print ("\nGood Riddance!\n")
