def add(a, b):
	return a + b
def sub(a, b):
	return a - b
def mul(a, b):
	return a * b
def div(a, b):
	return a / b

a = add(9.1, 8)
b = sub(9.1, 8)
c = mul(9.1, 8)
d = div(9.1, 8)

print "adding - " + str(a)
print "subtracting - " + str(b)
print "multiplying - " + str(c)
print "dividing - " + str(d)


def hours_from_seconds(seconds):
	hours = seconds / 3600
	return hours

hours = hours_from_seconds(86400)
print "hours_from_seconds - " + str(hours)

import math

def circle_area(radius):
	r_squared = radius * radius
	area = math.pi * r_squared
	return area

circlearea = circle_area(5)
print "circle_area - " + str(circlearea)

def sphere_volume(radius):
	r_cubed = radius * radius * radius
	fraction = float(4/3.0) 
	volume = fraction * math.pi * r_cubed
	return volume

spherevolume = sphere_volume(5)
print "sphere_volume - " + str(spherevolume) 

def avg_volume(x, y):
	a = x / 2
	b = y / 2
	a_volume = sphere_volume(a)
	b_volume = sphere_volume(b)
	together = a_volume + b_volume
	avg = together / 2.0
	return avg

avg_ = avg_volume(10, 20)
print "avg_volume - " + str(avg_)

def area(a, b, c):
	add_s = a + b + c
	s = 1/2.0 * add_s
	sub_a = s - a
	sub_b = s - b
	sub_c = s - c
	mul_eve = s * sub_a * sub_b * sub_c
	sqrt = math.sqrt(mul_eve)
	return sqrt

area_ = area(1, 2, 2.5)
print area_

def right_align(string):
	len_string = len(string)
	sub = 80 - len_string
	space = " "
	space_ = space * sub
	return space_ + string

rightalign = right_align("Hello")
print rightalign

def center(string):
	len_string = len(string)
	div_str = len_string / 2
	sub = 40 - div_str
	space = " "
	space_ = space * sub
	return space_ + string
	
center_ = center("Hello")
print center_

def msg_box("string"):
	len_string = len(string)
	length = len_string + 4
	
