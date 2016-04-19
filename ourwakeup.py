import math
	
#between 0 and 10
def range_(number):
	number_correct = 0
	sum_ = 0
	if number >= 0 and number < 10:
		number_correct = number_correct + 1
		sum_ = 0 + number
	else:
		print "{} is out of range.".format(number)
	average = sum_ / number_correct
	return average

# e = even o = odd
def O_E(average):
	int_average = int(average)
	if int_average % 2 == 0:
		return "even"
	else:
		return "odd"

def output(average, e_o):
	print """

The average is {}.
The integer part of the average is {}.
The integer part is {}.""".format(average, int(average), e_o)

def main():
	print """

This  program will ask you for 5 integer or float values.
It will calculate the average of all valus from 0 inclusive to 10 exclusive.
It will print out whether the resulting average is even or odd.

"""
	n_0 = float(raw_input("n0: "))
	n0 = range_(n_0)
	n_1 = float(raw_input("n1: "))
	n1 = range_(n_1)
	n_2 = float(raw_input("n2: "))
	n2 = range_(n_2)
	n_3 = float(raw_input("n3: "))
	n3 = range_(n_3)
	n_4 = float(raw_input("n4: "))
	n4 = range_(n_4)
	number_correct = n_4
	average = average_(n0, n1, n2, n3, n4, number_correct)
	o_e = O_E(average)
	return output(average, o_e)
	print output(average, o_e)

main()
	
