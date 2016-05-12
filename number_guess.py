import random
import math

def rounds(right_n, number_recursed, uc):
	user_n = raw_input("Guess: ")
	if right_n == int(user_n):
		print """you are correct
"""
		return uc + 1
	elif number_recursed == 0:
		return uc
	elif right_n < int(user_n):
		print "too high"
		return rounds(right_n, number_recursed - 1, uc)
	elif right_n > int(user_n):
		print "too low"
		return rounds(right_n, number_recursed - 1, uc)

def bonus(highest_number, lowest_number, number, computers_correct, number_recursed):
	print "I guess {}".format(number)
	your_number = raw_input("too (h)igh, too (l)ow, (c)orrect: ")
	if your_number == "c":
		computers_correct = computers_correct + 1
		return computers_correct
	elif number_recursed == 0:
		return computers_correct
	elif your_number == "h":
		bonus(number, lowest_number, ((number - highest_number) / 2) + number, computers_correct, number_recursed - 1)
	else:
		bonus(highest_number, number, ((highest_number - number) / 2) + number, computers_correct, number_recursed - 1)

def round_number(n, uc, cc):	
	if n == 0:
		print """
{} {}
""".format(str(uc), str(cc))
	else:
		right_n = 3
		print "\nYou have {} rounds left".format(n)
		uc = rounds(right_n, 4, uc)
		highest_number = 100
		lowest_number = 0
		number = 50
		computers_correct = 0
		cc = bonus(highest_number, lowest_number, number, computers_correct, 4) 
		round_number(n - 1, uc, cc)
	
def main():
	round_number(3, 0, 0)

main()
