#while x < 100:
	#print x
	#x += 1

def count_down(x):
	while x >= 0:
		print x 
		x -= 1

def countdown(x):
	if x > 0:
		while x >= 0:
			print x
			x -= 1
	else:
		while x <= 0:
			print x
			x += 1

def countFrom2(x, y):
	if x >= y:
		while x >= y:
			print y
			y += 1
	else:
		while y >= x:
			print x
			x += 1

def sumOfOdds(n):
	sumOfodds = 0
	if n > 0:
		while n >= 0:
			if n%2 != 0:
				sumOfodds += n
			n -= 1
	else:
		while n <= 0:
			if n%2 != 0:
				sumOfodds += n
			n += 1
	return sumOfodds

def grid(w, h):
	out = ""
	while h > 0:
		w = h
		while w != 0:
			out += "!"
			w -= 1
		out += "\n"	
		h -= 1
	return out
	
	
			

def main():
	print grid(5, 10)

main()

