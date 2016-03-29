# This game help you find the best position you should be in your basketball future.

import random

def output():
	print """
Greetings, Mr./Miss {}, welcome to BallDream Calculating Center once again. Today, we'll help you find out what position in basketball fits best for you.
""".format

def main():

	name = raw_input("What is your name?: ")
	height = raw_input("How tall are you (in cm)?: ")
	bballposition = raw_input("What position in basketball do you usually play?: ")
	if raw_input("How tall are you (in cm)?: ") > 195:
		print "You should be a Point Guard."
	elif raw_input("How tall are you (in cm)?: ") > 202 < 207:
		print "You should be a Shooting Guard."
	elif raw_input("How tall are you (in cm)?: ") > 207 < 210:
		print "You should be a Small Foward."
	elif raw_input("How tall are you (in cm)?: ") > 210 < 213:
		print "You should be a Power Foward."
	elif raw_input("How tall are you (in cm)?: ") < 214:
		print "You should be a Center."
	return main(name, height, bballposition)
	
