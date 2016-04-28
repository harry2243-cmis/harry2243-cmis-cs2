#def countdown(n):
#	if n<=0:	
#		print "blastoff"
#	else:
#		print n
#		countdown(n-1)
#	return
#
#
#def main():
#
#	countdown(10)
#
#main()


def adder(running_total = 0):
	print "The running total is {}".format(running_total)
	n0 = raw_input("next number: ")
	if n0 == "":
		print "The sum is {}".format(running_total)
	else:
		running_total += float(n0)
	
		adder(running_total)
adder()

