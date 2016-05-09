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

def bonus(cc, n, number_recursed):
	y_number = raw_input("too (h)igh, too (l)ow, (c)orrect: ")
	if y_number == "c":
		print "You're correct!"
		return cc + 1
	elif y_number == "h":
		n = (100 + n) / 2
		print "I guess {}".format(n)
		bonus(cc, n, number_recursed - 1)
	else:
		half_of = (100 - n)/2
		n = n + half_of
		print "I guess {}".format(n)
		bonus(cc, n, number_recursed - 1)

def round_number(n, uc):	
	if n == 0:
		print """
{} {}
""".format(str(uc, cc))
	else:
		right_n = random.randint(0, 100)
		print "\nYou have {} rounds left".format(n)
		uc = rounds(right_n, 4, uc)
		print "\nI guess 50"
		n = 50
		cc = bonus(0, 50, 4)
		round_number(n - 1, uc)
	
def main():
	round_number(3, 0)

main()
