#Section 1: Terminology
# 1) What is a recursive function?
# A recursive function is a function that calls itslef. (1)
#
#
# 2) What happens if there is no base case defined in a recursive function?
# If there is no base case defined in a recursive funtion then the funtion will keep on calling itself forever. (1)
#
#
# 3) What is the first thing to consider when designing a recursive function?
# The first thing to consider when desighing a recursive function in the base case. (1)
#
#
# 4) How do we put data into a function call?
# We put data into a function call in the form of arguments. (1)
#
# 
# 5) How do we get data out of a function call?
# We get data out of the funtion call by returning it with in the function. (1) 
#
#

#Section 2: Reading
# Read the following function definitions and function calls.
# Then determine the values of the variables a1-d3.

#a1 = 8 (1)
#a2 = 8 (1)
#a3 = -1 (1)

#b1 = 2 (1)
#b2 = 2 (1)
#b3 = -2 (-1)

#c1 = -2 (1)
#c2 = 4 (1)
#c3 = 45 (1)

#d1 = 4 (-1)
#d2 = 8 (1)
#d3 = 4 (1)

#Section 3: Programming
#Write a script that asks the user to enter a series of numbers.
#When the user types in nothing, it should return the average of all the odd numbers
#that were typed in. 
#In your code for the script, add a comment labeling the base case  on the line BEFORE the base case.
#Also add a comment label BEFORE the recursive case.
#It is NOT NECESSARY to print out a running total with each user input.

def odds(total_odds, number_odd):
	your_number = raw_input("Next: ")
	#base case
	if your_number == "":
		average = float(total_odds)/float(number_odd)
		print "The average of your odd numbers is {}".format(average)	
	#the next two are both recursive
	elif int(your_number)%2 == 0:
		odds(total_odds, number_odd)
	else:
		number_odd = number_odd + 1 
		total_odds = total_odds + int(your_number)
		odds(total_odds, number_odd)

def main():
	total_odds = 0
	number_odd = 0
	odds(total_odds, number_odd)
	

main()


