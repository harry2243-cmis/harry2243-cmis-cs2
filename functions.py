import math
def add(a,b):
	return a+b
print add(3,4)
# This adds a and b

def sub(a,b):
	return a-b
print sub(5,3)
# This suntracts a and b

def mul(a,b):
	return a*b
print mul(4,4)
# This times a and b

def div(a,b):
	return a/b
print div(2,3.0)
# This divides a and b

def hours_from_seconds(a,b):
	return a/b
print hours_from_seconds(86400,3600)
# This divides the time

def circle_area(a):
	return math.pi* a **2
print circle_area(5)
# This is a function that tells the area

def sphere_volume(radius):
	return 1.33333333333 * math.pi * (radius**3) #
print sphere_volume(5)
# This is a function that tells the volume

def avg_volume(diameter1, diameter2):
    vsphere1=volume(diameter1/2)
    vsphere2=volume(diameter2/2)
    return (vsphere1+vsphere2)/2
print avg_volume(10, 20)
# This is a function that tells the average volume

def area(a, b, c):
	return math.sqrt (2.75*(2.75-a)*(2.75-b)*(2.75-c))
print area(1.0, 2.0, 2.5)
# This is a function that tells the area

def right_align(word):
	return str ((80-len(word))*" " + word)
print right_align("Hello")
# This is a funtion that tells the right align

def center(term):
	return str ((40-len(term))*" " + term) 
print center ("Hello")
# This is a function that tells the center

def msg_box(word):
	return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+ 4)*"-") + "+" 
# This is a funtion that makes the message box
	
print msg_box("Hello")
print msg_box("I eat cats!")
# This prints the mesage boxes

a=add(3,4)
b=sub(5,3)
c=mul(4,4)
d=div(2,3.0)
e=divhrs(86400,3600)
f=area(5)
g=volume(5)
h=avg_volume(10, 20)
i=area2(1.0, 2.0, 2.5)
j=right_align("Hello")
k=center ("Hello")
l=msg_box("Hello")
m=msg_box("I eat cats!")

ab=add(8,2)
cd=sub(3,8)
ef=mul(9,9)
gh=div(4,8.0)
ij=divhrs(88400,4600)
kl=area(6)
mn=volume(2)
op=avg_volume(11, 25)
qr=area2(1.5, 3.0, 4.5)
p=right_align("Hey")
z=center ("Hens")
x=msg_box("Life")
y=msg_box("I eat for a living!")

print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(j)
print msg_box(k)
print l
print m
print msg_box(str(ab))
print msg_box(str(cd))
print msg_box(str(ef))
print msg_box(str(gh))
print msg_box(str(ij))
print msg_box(str(kl))
print msg_box(str(mn))
print msg_box(str(op))
print msg_box(str(qr))
print msg_box(p)
print msg_box(z)
print x
print y
