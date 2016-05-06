import random
import math

def rounds(right_n, number_recursed, c):
	user_n = raw_input("Guess: ")
	if right_n == int(user_n):
		print """you are correct
"""
		c = c + 1
		return c
	elif number_recursed == 0:
		print ""
	elif right_n < int(user_n):
		print "too high"
		return rounds(right_n, number_recursed - 1, c)
	elif right_n > int(user_n):
		print "too low"
		return rounds(right_n, number_recursed - 1, c)

def round_number(n, c):	
	if n == 0:
		print "You got {} correct".format(str(c))
	else:
		right_n = 5
		print "You have {} rounds left".format(n)
		c = rounds(right_n, 5, c)
		round_number(n - 1, c)
	
def main():
	round_number(3, 0)

main()
