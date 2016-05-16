#This game is to test your knowledge in basketball, and if you are a true fan of it.
import random

def intro():

	print "Welcome to BallDream Calculating Center once again! Today, we present to you, The Road To The Final."
	

	print "Hello, you are about to enter BallDream Calculating Center's The Road To The Final contest."
	print ("\n")

	print "The program will be testing your basketball knowledges, including thr NBA. So, without further ado, let's begin!"

	print ("\n")

def age():
	age = raw_input("Please type your age here :")
	random.randint(1,99)
	if age >= 15:
		print "YOUNG BOI!!"
	elif age < 15:
		print "U R OLD!!"
	else:
		return random.random()
	print ("\n")

def Warmup():
	
	print "Warm Up Question : Basketball is everyone's favorite sport. True or False?"

	Warmup_choice = raw_input("Please type your choice here")

	if Warmup_choice == "True" or "False":
		print "People have their own opinion in their favorite sports, this is just a warmup question. Let's begin the real deal!"
	
		print("\n")

def Warmup2():
	
	print "Warm Up Question 2 : Basketball is for cool people. True or False?"

	Warmup_choice2 = raw_input("Please type your choice here")

	if Warmup_choice2 == "True" or "False":
		print "People have their own opinion about basketball, this is just a warmup question. Let's begin the real deal!"
	
		print("\n")

def rookie():

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
	elif choice_3 == "Andrew Wiggins":
		print "You are wrong" 
	else:
		print "Sorry, you are wrong~~~~ Better luck next time!"
		exit()

		print("\n")

def Halloffame2():
	
	print "Q.4 : How many points did James Harden average in the 2011-12 NBA season?"

	choice_4 = raw_input("Please type your choice here - 12.2 or 16.8")

	if choice_4 == "16.8":
		print "You are correct!"
	elif choice_4 > "12.2":
		print "You are wrong" 
	else:
		print "Sorry, you are wrong~~~~ Better luck next time!"
		exit()

		print("\n")

def End():

	print "Wow, you did it!"
	print "Congradulation! You have passed the BallDream Calculating Center, The Road To The Final program!"
	print("\n")
	
def main():
	intro()
	age()
	Warmup()
	Warmup2()
	rookie()
	Allstar()
	Halloffame()
	Halloffame2()
	End()
main()	
