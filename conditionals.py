#This game is to test your knowledge in basketball, and if you are a true fan of it.
import random

def Rookie():

	print """ "Welcome to BallDream Calculating Center once again! Today, we present to you, The Road To The Final."

"Hello, you are about to enter BallDream Calculating Center's The Road To The Final contest."

"The program will be testing your basketball knowledges, including thr NBA. So, without further ado, let's begin!"
"""

def pro():

	print """Q.1 : Who is the father/creator, of basketball?"
 "James Naismith, or Walter Camp?" """


	choice_1 =raw_input("Please type your choice here ")
	
	if choice_1 == "James Naismith":
		print "You are correct! James Naismith invented the sport of basketball in 1891."
	else: 
		print "Sorry, you are wrong~~~~ Better luck next time!"
		exit()
	print ("\n")
	

def Allstar():

	print "Q.2 : What foul do you call, when a player carried the ball, instead of dribbling the ball?"
	print "Double drible, or travel?"

	choice_2 = raw_input("Please type your choice here ")

	if choice_2 == "travel":
		print "You are correct!"
	elif choice_2 == "Double drible":
		print "You are wrong"
	else:
		print "Sorry, you are wrong~~~~ Better luck next time!"
		quit()

	print("\n")
	

def Halloffame():
	
	print "Q.3 : Who was drafted first in the 2015 NBA Draft?"
	print "Karl Anthony Towns, or Andrew Wiggins?"

	choice_3 = raw_input("Please type your choice here")

	if choice_3 == "Karl Anthony Towns":
		print "You are correct!"
	elif choice_3 == "Andrew Wiggins":
		print "You are wrong!"
	else:
		print "Sorry, you are wrong~~~~ Better luck next time!"
		exit()

		print("\n")

def godlike():

	print "Q.4 : Who did the Rockets hire as their 2016-17 coach?"
	print "Jeff Van Gundy, or Mike D'Antoni?"

	choice_4 = raw_input("Please type your choice here ")

	if choice_4 == "Mike D'Antoni":
		print "You are correct!"
	else:
		print "Sorry, you are wrong~~~~ Better luck next time!"
		quit()

	print("\n")

def Opinion():

	print "Basketball is the best sport?"
	print "Yes or No?"

	choice_4 = raw_input("Please type your choice here ")

	if choice_4 == "Yes":
		return True
	else:
		return False
		quit()

	print("\n")

def Bonus():
	choice_5= raw_input("What is James Harden's height? (For fun)")
	if choice_5 == 196:
		return 1
	elif choice_5 >= 196 and choice_5 <= 190:
		print "You are close"
	elif choice_5 < 180 or choice_5 >200:
		print "Bette luck next time~"
	elif not choice_5 <170:
		print 0
	else:
		return 0

def ring():
	choice_6=raw_input("How many total ring does the Boston Celtics currently have?")
	if choice_6 == 17:
		return random.randint(1,5)
	else:
		return random.random
	
	
def End():

	print """ "Wow, you did it!"
"Congradulation! You have passed the BallDream Calculating Center, The Road To The Final program!"
"""
	
def main():
	Rookie()
	pro()
	Allstar()
	Halloffame()
	godlike()
	Opinion()
	Bonus()
	ring()
	End()
main()	
