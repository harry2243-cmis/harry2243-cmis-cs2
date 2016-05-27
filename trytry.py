def countdown(x):
	while x >=0:
		print x
		x-=1

def countup(x):
	while x<10:
		print x
		x+=1
def count(x):
	while x < 0:
		print x
		x+=1
	while x >0:
		print x
		x-=1

def addodd():
	while n<9:
		print n
		n+=1

def grid(w, h):
	out = ","*w*h
	print out

def main():
	grid(50, 40)
main()

