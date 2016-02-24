import math

def add(a, b):
	return a + b
def sub(a, b):
	return a - b
def mul(a, b):
	return a * b
def div(a, b):
	return float(a) / float(b)

a = add(9.1, 8.3)
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

def avg_volume(diameter_1, diameter_2):
	radius_a = diameter_1 / 2
	radius_b = diameter_2 / 2
	a_volume = sphere_volume(radius_a)
	b_volume = sphere_volume(radius_b)
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
	sqrt_ = math.sqrt(mul_eve)
	return sqrt_

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

def msg_box(string):
	string = string
	len_string = len(string)
	length = len_string + 4
	dashed = "-" * length
	return "+" + str(dashed) + "+ \n" + "|  " + str(string) + "  | \n" + "+" + str(dashed) + "+"

box_hello = msg_box("Hello")
print box_hello
	
box_cats = msg_box("I like cats!")
print box_cats


add__ = add(9.1, 8)
print msg_box(str(add__))
add_ = add(9.2, 9)
print msg_box(str(add_))

sub__ = sub(9.1, 8)
print msg_box(str(sub__))
sub_ = sub(91, 86)
print msg_box(str(sub_))

mul__ = mul(9.1, 8)
print msg_box(str(mul__))
mul_ = mul(41, 85)
print msg_box(str(mul_))

div__ = div(9, 8)
print msg_box(str(div__))
div_ = div(1, 8)
print msg_box(str(div_))

hours = hours_from_seconds(86400)
print msg_box("hours_from_seconds - " + str(hours))
hours = hours_from_seconds(565656565656565)
print msg_box("hours_from_seconds - " + str(hours))

circlearea = circle_area(5)
print msg_box("circle_area - " + str(circlearea))
circlearea = circle_area(67.875342)
print msg_box("circle_area - " + str(circlearea))

spherevolume = sphere_volume(5)
print msg_box("sphere_volume - " + str(spherevolume)) 
spherevolume = sphere_volume(66666777.345)
print msg_box("sphere_volume - " + str(spherevolume))

avg_ = avg_volume(10, 20)
print msg_box("avg_volume - " + str(avg_))
avg_ = avg_volume(5, 24)
print msg_box("avg_volume - " + str(avg_))

area_ = area(1, 2, 2.5)
print msg_box(str(area_))
area_ = area(10, 20, 23)
print msg_box(str(area_))

rightalign = right_align("Hello")
print msg_box(rightalign)
rightalign = right_align("Goodbye")
print msg_box(rightalign)

center_ = center("Hello")
print msg_box(center_)
center_ = center("Goodbye")
print msg_box(center_)

box_hello = msg_box("Hello")
print box_hello
box_hello = msg_box("Goodbye")
print box_hello
	
box_cats = msg_box("I like cats!")
print box_cats
box_cats = msg_box("I hate cats!")
print box_cats
