import random

def Rookie():

	print "Welcome to BallDream Calculating Center once again! Today, we present to you, The Road To The Final."
	

	print "Hello, you are about to enter BallDream Calculating Center's The Road To The Final contest."
	print ("\n")

	print "The program will be testing your basketball knowledges, including thr NBA. So, without further ado, let's begin!"

	print ("\n")

	print "Q.1 : Who is the father/creator, of basketball?"
	print " James Naismith, or Walter Camp?"

	print ("\n")

	choice_1 =raw_input("Please type your choice here ")
	
	print("\n")

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
	else:
		print "Sorry, you are wrong~~~~ Better luck next time!"
		exit()

		print("\n")

def End():

	print "Wow, you did it!"
	print "Congradulation! You have passed the BallDream Calculating Center, The Road To The Final program!"
	print("\n")
	
def main():
	Rookie()
	Allstar()
	Halloffame()
	End()
main()	
