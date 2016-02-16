def mul(a, b):
	c = a * b
	return c

def output(a, b, d):
	return "{} x {} = {}".format(a, b, d)

def main():
	a = raw_input("Type a number: ")
	b = raw_input("Type another number: ")
	d = mul(int(a), int(b))
	print output(a, b, d)

main()
