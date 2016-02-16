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
print "hours in sconds - " + str(hours)

import math

def circle_area(radius):
	r_squared = radius * radius
	area = math.pi * r_squared
	return area

circlearea = circle_area(5)
print "area of a circle - " + str(circlearea)

def sphere_volume(radius):
	r_cubed = radius * radius * radius
	fraction = float(4/3.0) 
	volume = fraction * math.pi * r_cubed
	return volume

spherevolume = sphere_volume(5)
print "sphere volume - " + str(spherevolume) 

def avg_volume(x, y):
	a = x / 2
	b = y / 2
	a_volume = sphere_volume(a)
	b_volume = sphere_volume(b)
	together = a_volume + b_volume
	avg = together / 2.0
	return avg

avg_ = avg_volume(10, 20)
print "average sphere volume - " + str(avg_)

