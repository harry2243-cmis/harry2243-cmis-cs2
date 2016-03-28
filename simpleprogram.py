import math

def avgpoints(firstGame,secondGame):
	return (float(firstGame)+ float(secondGame))/2
	

def output(name, whereAttend, avg):
	print """
Greetings, Mr./Miss {}, welcome to BallDream Calculating Center. You currently attend {}. You average around {} points from your recent 2 games.
""".format(name, whereAttend, avg)
	
def main():
	
	name = raw_input("What is your name?: ")
	whereAttend = raw_input("Which school do you attend?: ")
	firstGame = raw_input("How much points did you score in your game 2 games ago?: ")
	secondGame = raw_input("How much points did you score in your latest game?: ")
	avg= avgpoints(float(firstGame),float(secondGame))
	
	return output(name, whereAttend, avg)	
main()



