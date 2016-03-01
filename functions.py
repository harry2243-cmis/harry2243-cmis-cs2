import math

def add(a, b):
	return a + b
print add(3, 4)

def sub(a, b):
	return a - b
print sub(5, 3)

def mul(a, b):
	return a * b
print mul(4, 4)

def div(a, b):
	return float(a) / b
print div(2, 3)

def divhrs(a, b):
	return a / b
print divhrs(86400, 3600)

def multi(a, b):
	return math.pi* a **2
print multi(5,2)

def volume(a):
	return (((4/3.0)*math.pi)*a**3)
print volume(5)

def avg_volume (a, b):
	 return ((1.0/6 * math.pi * a**3) + (1.0/6 * math.pi * b**3)) /2
print avg_volume(10, 20)

def area(a, b, c):
	x = (a + b + c)/2
	return math.sqrt(x*(x-a)*(x-b)*(x-c))

def right_align(word):
	return str ((80-len(word))*" " + word)
	
print right_align("Hello")

def center(term):
	return str ((40-len(term))*" " + term) 
	
print center ("Hello")
	
def msg_box(word):
	return "+" + ((len(word)+ 4)*"-") + "+" + "\n" + "|" + (2*" ") + (word) + (2*" ") + "|" + "\n" + "+" + ((len(word)+ 4)*"-") + "+"
	
print msg_box("Hello")
print msg_box("I eat cats!")

a = add(3, 11)
b = add(4, 12)
c = sub(2, 1234)
d = sub(5, 56)
e = mul(4, 467)
f = mul(7, 6789)
g = div(34567, 7893675)
h = div(51231, 18668)
i = divhrs(262345, 598757867)
j = divhrs(3, 78)
k = multi(2345, 67969)
l = multi(857, 728472)
m = volume(4)
n = volume(87)
o = avg_volume(876, 98766)
p = avg_volume(6, 87)
q = area(1, 2, 3)
r = area(3, 2, 1)
s = right_align("hello")
t = right_align("rekt")
u = center("iwaswondering")
v = center("blahblahblah")
w = msg_box("hellofromthe")
x = msg_box("otherside")	
print msg_box(str(a))
print msg_box(str(b))
print msg_box(str(c))
print msg_box(str(d))
print msg_box(str(e))
print msg_box(str(f))
print msg_box(str(g))
print msg_box(str(h))
print msg_box(str(i))
print msg_box(str(j))
print msg_box(str(k))
print msg_box(str(l))
print msg_box(str(m))
print msg_box(str(n))
print msg_box(str(o))
print msg_box(str(p))
print msg_box(str(q))
print msg_box(str(r))
print msg_box(str(s))
print msg_box(str(t))
print msg_box(str(u))
print msg_box(str(v))
print msg_box(str(w))

