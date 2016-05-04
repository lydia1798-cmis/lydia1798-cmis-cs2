import random
import math

def rounds(right_n, number_recursed):
	user_n = raw_input("Guess: ")
	if right_n == int(user_n):
		print "you are correct"
		return 1
	elif number_recursed == 0:
		print ""
	elif right_n < int(user_n):
		print "too high"
		return rounds(right_n, number_recursed - 1)
	elif right_n > int(user_n):
		print "too low"
		return rounds(right_n, number_recursed - 1)

def round_number(n):
	if n == 0:
		return "You got {} correct".format(str"rounds")
	else:
		right_n = random.randint(0, 100)
		print "You have {} rounds left".format(n)
		round_ = rounds(right_n, 5)
		round_number(n - 1)
	
def main():
	n = 3
	round_number(n)
main()
