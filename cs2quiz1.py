#Part 1: Terminology (15 points)
#1 1pt) What is the symbol "=" used for?
# The symbol is the assignment operator. It creates new variables. It also gives them values when created.
#
#
#2 3pts) Write a technical definition for 'function'
# A function is a sequence of statements that is named, and performs a computation. When you define a function, you'll need to specify the sequence of the statement, and the name.
# 
#
#3 1pt) What does the keyword "return" do?
# It is called the argument of the function. THe function will take an argument and return a result, and the result is called a return value.
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below
#	1:or (4>2 or 2>4) (4566>1234 or 1234>4566)
#	2:and (8 == 8 and 7 == 7) (87>8 and 10<89)
#	3:not (5>3 not 3>5) (1234<9988 not 9988<1234)
#	4:if (true == false - if - false == true) (6>8 if 8<6) 
#	5:is (1 is 1.0) (8 is 8.0)
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"?
#A function definition is defining the function. A function call is calling the function using numbers, or you can use variables. 
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them
#	1:int() -  This will use the string/number and turns it into an integer. It does it so that you can use it to do math problems.
#	2:float() - This will take anything and put it into a string. By doing that, you can print out a sentence with numbers.
#	3:str() - :This takes any number/integer and it will turn it into a decimal.
#
#Part 2: Programming (25 points)
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi

import math

c1 = raw_input("The area of C1:")
c2 = raw_input("The area of C2:")
c3 = raw_input("The area of C3:")

def cir_dia(area):
	 return math.sqrt(((area) / math.pi)) + math.sqrt(((area) / math.pi))

print ""

cir_dia1 = math.sqrt(((float(C1)) / math.pi)) + math.sqrt(((float(C1)) / math.pi))
cir_dia2 = math.sqrt(((float(C2)) / math.pi)) + math.sqrt(((float(C2)) / math.pi))
cir_dia3 = math.sqrt(((float(C3)) / math.pi)) + math.sqrt(((float(C3)) / math.pi))

Total = float(cir_dia1) + float(cir_dia2) + float(cir_dia3)

print "Circle Diameter"
print "cir_dia1 " + str(C1)
print "cir_dia2" + str(C2)
print "cir_dia3 " + str(C3)
print "Totals " + str(Total)
