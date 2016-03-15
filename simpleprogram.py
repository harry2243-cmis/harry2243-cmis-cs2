def main():

	name = raw_input("What is your name?: ")
	whereAttend = raw_input("Which school do you attend?:")
	firstGame = raw_input("How much points, assists, and rebounds did you score in your game 2 games ago?: ")
	secondGame = raw_input("How much points, assists, and rebounds did you score in your latest game?: ")
	return output()

def output():
	print """
Greetings, Mr./Miss {}, welcome to BallDream Calculating Center. You currently attend {}. You average around {} points, {} assists, and {} rebounds from your recent 2 games.

