#PART 1: Terminology
#1) Give 3 examples of boolean expressions.
#a) if 45 == 45
#b) 12 > 10
#c) not 34 == 87
#
#2) What does 'return' do?
# Return gives you the result of the function. It is different than print because it doesn't print anything out. It just returns the result. 
#
#
#
#3) What are 2 ways indentation is important in python code?
#a) One way is it shows you when the function ends
#b) when you are using if, elif and else. You need to indent to show what you are using in that function
#
#

#PART 2: Reading
#Type the values for 12 of the 16 of the variables below.
#
#problem1_a) 36 
#problem1_b) square root of 3
#problem1_c) square root of 0
#problem1_d) -5
#
#problem2_a) True
#problem2_b) False
#problem2_c) False
#problem2_d) False
#
#problem3_a) c
#problem3_b) b
#problem3_c) a
#problem3_d) b
#
#problem4_a) 7
#problem4_b) 5
#problem4_c) 1.25
#problem4_d) 5
#

#PART 3: Programming
#Write a script that asks the user to type in 3 different numbers.
#If the user types 3 different numbers the script should then print out the
#largest of the 3 numbers.
#If they don't, it should print a message telling them they didn't follow 
#the directions.
#Be sure to use the program structure you've learned (main function, processing function, output function)

import math

def greater_less_than(n1, n2, n3): #I couldn't figure out what to call it.
	if n1 > n2 and n1 > n3:
		return "The largest number was {}.".format(n1)
	elif n2 > n1 and n2 > n3:
		return "The largest number was {}.".format(n2)
	elif n3 > n1 and n3 > n2:
		return "The largest number was {}.".format(n3)
	elif n1 == n2 or n1 == n3 or n2 == n3:
		return "You didn't follow directions."

#do I need to put else at the end?
#I don't think I need an out put function

def main():
	print "Type in 3 different numbers (decimals are OK!)" #I don't know how to put that into and output function
	n1 = float(raw_input("A: "))
	n2 = float(raw_input("B: "))
	n3 = float(raw_input("C: "))
	end = greater_less_than(n1, n2, n3)
	print end
	
main()
