#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) 1>3
#b) 5>2*2-3
#c) 74>=2*2*3
# +3
#2) What does 'return' do?
# 'return' helps call the def/function. It also help split the value
#
# +1
#
#3) What are 2 ways indentation is important in python code?
#a) Identation makes the python code work.
#b) Identation for 'return' or python codes after 'def', helps the code to work.
#
# +2

#PART 2: Reading
#Type the values for 9 of the 12 of the variables below.
#
#problem1_a) = -36 (+1)
#problem1_b) = -3 (+1)
#problem1_c) = 0 (+1)
#problem1_d) = -5 (+1) 
#
#problem2_a) = True (+1)
#problem2_b) = False (+1)
#problem2_c) = False (+1)
#problem2_d) = True (+1)
#
#problem3_a) = 0.3 (+1)
#problem3_b) = 0.5 (+1)
#problem3_c) = 0.5 (+1)
#problem3_d) = 0.5 (+1)
#
#problem4_a) = 7 (+1)
#problem4_b) = 5 (+1)
#problem4_c) = 12.5 
#problem4_d) = 5 (+1)
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

#Q23 +1

def output(numberone, numbertwo, numberthree):
	print """
"Type in 3 different numbers (decimals are ok)"
"""

def main():

	numberone = raw_input("A: ") 
	numbertwo = raw_input("B: ")
	numberthree = raw_input("C: ")
	return cal

#Q30 +1
def cal(): 
	Anumber = math(float(numberone))
	Bnumber = math(float(numbertwo))
	Cnumber = math(float(numberthree))
	return output

def ans():

	ans = raw_input("Your Answer is {}")
	return ans

main()




