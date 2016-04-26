def countdown_from_to(start, stop):
	if start<stop:
		print 'Blastoff'
	else: 
		print start
		countdown_from_to(start-1, stop)


def main():

	
	countdown_from_to(7, 2)

main()
