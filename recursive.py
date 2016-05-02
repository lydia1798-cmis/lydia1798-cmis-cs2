def countdown(n):
	if n <= 0:
		print "The countdown has ended...unicorns will now inhabit the earth."
	else:
		print n
		countdown(n - 1)

def countup(n):
	if n >= 11:
		print "The countup has ended...tacos will now fall from the sky"
	else:
		print n
		countup(n + 1)
	

def countup_from(start, stop):
	if start >= stop + 1:
		print "Free pizza! Just kidding, dreams don't come true."
	else:
		print start
		countup_from(start + 1, stop)

def countdown_from(start, stop):
	if start <= stop - 1:
		print "yay!"
	else:
		print start
		countdown_from(start - 1, stop)

def adder(sum):
	print "Running total: {}".format(sum)
	input_number = raw_input("Next Number: ")
	if input_number == "":
		print "The sum is {}.".format(sum)
	else:
		sum = sum + float(input_number)
		adder(sum)
		
def biggest(number):
	input_number = raw_input("Next: ")
	if input_number == "":
		return number
	elif number < float(input_number):
			number = float(input_number)
			return biggest(number)
	else:
		number = number 
		return biggest(number)

def smallest(number):
	input_number = raw_input("Next: ")
	if input_number == "":
		return number
	elif number < float(input_number):
		number = number
		return smallest(number)
	else:
		number = float(input_number) 
		return smallest(number)	

def pow(x, n):
	if n == 0:
		return 1
	else:
		return x * pow(x, n - 1)
	
def main():
	countdown(10)
	countup(1)
	countup_from(1, 10)
	countdown_from(15, -8)
	sum = 0
	adder(sum)
	number_biggest = float("-inf")
	print biggest(number_biggest)
	number_smallest = float("+inf")
	print smallest(number_smallest)
	print pow(3, 2)

main()
		
