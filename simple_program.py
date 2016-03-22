import math

def distance(x_1, y_1, x_2, y_2):
	x = abs(x_2 - x_1)
	y = abs(y_2 - y_1)
	x_sqrd = x ** 2
	y_sqrd = y ** 2
	add = x_sqrd + y_sqrd
	sqrt = math.sqrt(add)
	return sqrt
	

def output(c):
	return "The distance between your two coordinate pairs: {}".format(c)

def main():
	x_1 = float(raw_input("Type the x in the first coordinate pair: "))
	y_1 = float(raw_input("Type the y in the first coordinate pair: "))
	x_2 = float(raw_input("Type the x in the second coordinate pair: "))
	y_2 = float(raw_input("Type the y in the secind coordinate pair: "))
	TheDistance = distance(x_1, y_1, x_2, y_2)
	print output(TheDistance)

main()


