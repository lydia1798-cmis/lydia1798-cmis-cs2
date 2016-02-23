import math

n = 2

def add(a, b):
	c = a + b
	return c

def sub(x_1, x_2):
	a = x_1 - x_2
	return a

def pow_(a):
	math.pow(a, n)
	return a**n

def sqrt(b):
	b_sqrt = math.sqrt(b)
	return b_sqrt

def output(c):
	return "The distance between your two coordinate pairs: {}".format(c)

def main():
	x_1 = raw_input("Type the x in the first coordinate pair: ")
	y_1 = raw_input("Type the y in the first coordinate pair: ")
	x_2 = raw_input("Type the x in the second coordinate pair: ")
	y_2 = raw_input("Type the y in the secind coordinate pair: ")
	a = sub(float(x_1), float(x_2))
	b = sub(float(y_1), float(y_2))
	c = pow_(float(a))
	d = pow_(float(b))
	sum_ = add(float(c), float(d))
	sqrt_ = sqrt(float(sum_))
	print output(sqrt_)

main()


