import random

#the number you are comparing things with
def THEtarget(minimum, maximum):
	target = random.randint(minimum, maximum)
	return target

#Getting the minimum and maximum and doing the comparison. You find the target number in main with the raw input and the THEtarget function. 
def main():
	minimum = int(raw_input("What is the minimum number?: "))
	maximum = int(raw_input("What is the maximum number?: "))
	print "I'm thinking of a number from", minimum, "to", maximum, "."
	target = THEtarget(minimum, maximum)
	your_number = int(raw_input("What do you think it is?: "))
	if target == your_number: 
		print """
Your target was {}.
Your guess was {}.
That's correct! You must be psychic!
		""".format(target, your_number)
	elif target > your_number:
		sub = target - your_number
		print """
Your target was {}.
Your guess was {}.
That's under by {}.
		""".format(target, your_number, sub)
	elif target < your_number:
		sub = your_number - target 
		print """
Your target was {}.
Your guess was {}.
That's over by {}.
		""".format(target, your_number, sub)
#cant do else because then it wil be automatic

main()	
