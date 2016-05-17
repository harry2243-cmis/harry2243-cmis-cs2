#Section 1: Terminology
# 1) What is a recursive function?
# Recursive function is a function that either calls itself, or it's in a function call. It is also a function that recurse.
#
#
# 2) What happens if there is no base case defined in a recursive function?
# The function won't work. 'if' won't work. It also wouldn't be complete.
#
#
# 3) What is the first thing to consider when designing a recursive function?
# Have the base case. Without the base case, it won't work well.
#
#
# 4) How do we put data into a function call?
# You need to use a parameter, I think.
#
# 
# 5) How do we get data out of a function call?
# You put it into a variable. 
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables q1-q20.

#a1 = 8
#a2 = 8
#a3 = -1

#b1 = 2
#b2 = 2
#b3 = 1

#c1 = -2
#c2 = 4
#c3 = 45

#d1 = 6 
#d2 = 8 
#d3 = 4

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

