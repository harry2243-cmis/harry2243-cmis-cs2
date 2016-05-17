#Section 1: Terminology
# 1) What is a recursive function?
# Recursive function is a function that either calls itself, or it's in a function call.
#
#
# 2) What happens if there is no base case defined in a recursive function?
# The function won't work. 'if' won't work.
#
#
# 3) What is the first thing to consider when designing a recursive function?
# Have the base case and the recursive case. Makes sure they work well.
#
#
# 4) How do we put data into a function call?
#
#
# 
# 5) How do we get data out of a function call?
#
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 2, 11
#a2 = 11, 2
#a3 = 1, 0

#b1 = 4, 4
#b2 = 1, 1
#b3 = -1, 4

#c1 = 1, 0
#c2 = 2, 1
#c3 = 10, 9

#d1 =
#d2 =
#d3 =

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

import random


def adder(numbers = 1):
	print "The current total is {}".format(numbers)
	n0 = raw_input("Please type in the next number: ")
	if n0 == "":
		print "The sum is {}".format(numbers)
	else:
		numbers += float(n0)
	
		adder(numbers)

def main():
	adder()
main()

