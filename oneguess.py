import random
import math

def THEtarget(minimum, maximum):
	target = random.radiant(minimum, maximum)
	return target


def less(target, your_number):
	if target < your_number
		sub = your_number - target 
		return """
		Your target was {}.
		Your guess was {}.
		That's over by {}.
		""".format(target, your_number, sub)
	 
def main():
	minimum = int(raw_input("What is the minimum number?"))
	maximum = int(raw_input("What is the maximum number?"))
	print "I'm thinking of a number from", minimum, "to", maximum, "."
	target = THEnumber(minimum, maximum)
	your_number = int(raw_input("What do you think it is?: "))
	if target == your_number 
		return """
		Your target was {}.
		Your guess was {}.
		That's correct! You must be psychic!
		""".format(target, your_number)
	elif target > your_number
		sub = target - your_number
		return """
		Your target was {}.
		Your guess was {}.
		That's under by {}.
		""".format(target, your_number, sub)
	elif target < your_number
		sub = your_number - target 
		return """
		Your target was {}.
		Your guess was {}.
		That's over by {}.
		""".format(target, your_number, sub)


main()
	
	

