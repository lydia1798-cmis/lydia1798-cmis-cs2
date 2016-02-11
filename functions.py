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

print a
print b
print c
print d


def hours_from_seconds(seconds):
	hours = seconds / 3600
	return hours

hours = hours_from_seconds(86400)
print hours

import math

def circle_area(radius):
	diameter = radius * 2
	area = diameter * math.pi
	return area

circlearea = circle_area(5)
print circlearea


NOT RIGHT

