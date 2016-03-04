
#Part 1: Terminology (15 points)-12.5/15 points
#Programming-24/25 points
#1 1pt) What is the symbol "=" used for? (1)
# Used to put calue into a variable, called an assignment operator. 
#
#
#2 3pts) Write a technical definition for 'function' (3)
#A function is a named sequence of statements that performs a computation.
#
#
#3 1pt) What does the keyword "return" do? (1)
#Return just gives you back the result of your progra, however it does not print it. 
#
#
#4 5pts) We know 5 basic data types. Write the name for each one and provide two
#   examples of each below (2.5)
#	1: String
#	2: Float
#	3: Integer
#	4: boolean
#	5: tuple
#
#5 2pts) What is the difference between a "function definition" and a 
#        "function call"? (2)
# A function definition is where you are writing the function and telling it what to do. When you call a function, however, you are taking that function (definition) and you are plugging some values into it and getting something back (ex. len(4, 5)).
#
#
#
#6 3pts) What are the 3 phases that every computer program has? What happens in
#        each of them (3)
#	1: input (source code) - you are putting something into the program
#	2: processing -  figures out what the program does and does it
#	3: output - it returns to you the result of that program
#
#
#Part 2: Programming (25 points)-23/25 points
#Write a program that asks the user for the areas of 3 circles.
#It should then calculate the diameter of each and the sum of the diameters 
#of the 3 circles.
#Finally, it should produce output like this:

#Circle  Diameter
#c1      ...
#c2      ...
#c3      ...
#TOTALS  ...

# Hint: Radius is the square root of the area divided by pi


import math

#1 pt for header line (1)
#3 pt for correct formula (3)
#1 pt for return value (1)
#1 pt for parameter name (1)
#1 pt for function name (1)

def diameter(area):
	radius_sqrd = area / math.pi
	radius = math.sqrt(radius_sqrd)
	diameter = radius * 2
	return diameter

#1pt for header line (1)
#1pt for parameter names (1)
#1pt for return value (1)
#1pt for correct output format (1)
#3pt for correct use of format function (3)

def output(c1, c2, c3, total):
	return """
Circle  Diameter
c1  {}   
c2  {}   
c3  {}     
TOTALS  {}
""".format (c1, c2, c3, total)

#1pt header line (1)
#1pt getting input (1)
#1pt converting input (1)
#1pt for calling output function (1)
#2pt for correct diameter formula (2)
#1pt for variable names (1)

def main():
	c1_area = raw_input("Area of C1: ")
	c2_area = raw_input("Area of C2: ")
	c3_area = raw_input("Area of C3: ")
	c1 = diameter(float(c1_area))
	c2 = diameter(float(c2_area))
	c3 = diameter(float(c3_area))
	total = c1 + c2 + c3
	print output(c1, c2, c3, total)

#1pt for calling main (1) 

main()

#1pt explanatory comments (0)
#1pt code format (1)

