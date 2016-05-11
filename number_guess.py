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

def bonus(cc, computers_number, number_recursed):
	y_number = raw_input("too (h)igh, too (l)ow, (c)orrect: ")
	lowest_computers_number
	if y_number == "c":
		print "You're correct!"
		cc = cc + 1
		return cc
	elif number_recursed == 0:
		return cc
	elif y_number == "l":
		lowest_computers_number = computers_number
		computers_number = (lowest_computers_number + highest_computers_number / 2) + computers_number
		print "I guess {}".format(computers_number)
		bonus(cc, computers_number, number_recursed - 1)
	elif y_number == "h":
		highest_computers_number = computers_number 
		computers_number = lowest_computers_number + highest_computers_number/ 2
		print "I guess {}".format(computers_number)
		bonus(cc, computers_number, number_recursed - 1)

def round_number(n, uc, cc):	
	if n == 0:
		print """
{} {}
""".format(str(uc), str(cc))
	else:
		right_n = 3
		print "\nYou have {} rounds left".format(n)
		uc = rounds(right_n, 4, uc)
		print "\nI guess 50"
		computers_number = 50

		cc = bonus(0, 50, 4)
		round_number(n - 1, uc, cc)
	
def main():
	round_number(3, 0, 0)

main()
