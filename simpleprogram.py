import math

def output(name, whereAttend, avgPoints):
	print """
Greetings, Mr./Miss {}, welcome to BallDream Calculating Center. You currently attend {}. You average around {} points from your recent 2 games.
""".format(name, whereAttend, avgPoints)
	
def cal(firstGame, secondGame):
	avgPoints = int((firstGame + secondGame))/2
	return avgPoints
def main():
	
	name = raw_input("What is your name?: ")
	whereAttend = raw_input("Which school do you attend?:")
	firstGame = raw_input("How much points did you score in your game 2 games ago?: ")
	secondGame = raw_input("How much points did you score in your latest game?: ")
	avg = cal(firstGame, secondGame)
	return output(name, whereAttend, avg)	
main()



