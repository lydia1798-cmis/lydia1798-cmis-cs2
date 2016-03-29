# My script will be of a fight. You are walking along a path in the forest when you come upon a monster. "Do you want to fight with it?" If you say yes then you will keep playing if you say no then the moster will kill you. If you say yes, then you have to get ready to fight. The first question that you will be asked is "How old are you?" If you are from 1-14 then you get 9 lives added and one extra life by how far away from zero you are. If you are 14+ then you get 9 lives subtracted and a life added by how far away from zero you are. The second question that you will be asked is "Chose a pill, 1, 2, 3, 4 or a wild card." If you chose #1 = 100 strengths + 25 defenses. #2 = 75 strengths + 50 defenses. #3 = 50 stregths + 75 defenses. #4 = 25 strengths + 100 defenses. If you chose random it will take a random number from 1-100 for each defense and strength. Next you will be asked "Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand." Sword & sheild = If strength is more than 50 & defense is less than 50 then you win. If not you lose. Gun = If strenght is more than 25 and defense is less than 75 then you win. Bow and arrow = If strength is more than 0 and defense is more than 50 then you win. Magical wand = you always win but you will be teleported anywhere in the world. Then you will 'fight' with the monster and you will either win (you live) or you lose (you die).

#The questions that are going to be asked:
#	1. "Do you want to fight with it?" (yes, no)
#	2. "How old are you?" (your age)
#	3. "Chose a pill, 1, 2, 3, 4 or random." (1, 2, 3, 4, random)
#	4. "Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand." (sword & sheild, a gun, a bow & arrow and a magical wand)

#The story line:
#	"You are walking along a path in a forest and you come upon a monster. (Q.1) 'Do you want to fight it?' (yes, no)
#	No: You have chosen not to fight. Unfortuantly this has made it easier for the monster to kill you and you have just died.
#	Yes: "Get ready to fight....."
#		(Q.2) 'How old are you?' (your age)
#		(Q.3) 'Chose a pill, 1, 2, 3, 4 or random' (1, 2, 3, 4 or random) - If you chose #1 = 100 strengths + 25 defenses. #2 = 75 strengths + 50 defenses. #3 = 50 stregths + 75 defenses. #4 = 25 strengths + 100 defenses. If you chose random it will take a random number from 1-100 for each defense and strength.
#		(Q.4) 'Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand." (sword & sheild, a gun, a bow & arrow and a magical wand) - 
# Sword & sheild = If strength is more than 50 & defense is less than 50 then you win. If not you lose.
# Gun = If strenght is more than 25 and defense is less than 75 then you win.
# Bow and arrow = If strength is more than 0 and defense is more than 50 then you win.
# Magical wand = you always win but you will be teleported anywhere in the world.
#	"You have {} lives.
#	"Your strength is at {}.
#	"Your defense is at {}.
#	"You have a {}.
#
#	"The monster comes at you and since you have *weapon* you win!
#								OR
#	"The monster comes at you but since you have *weapon* you lose....

import random

def choice(desicion):
	if desicion == yes:
		print "You have chosen to fight..."
	else:
		print "You have chosen not to fight, giving the enemy the upper hand and you are killed. Try again."	

#The number of lives that you will have
def lives(age):
	if age <= 13: 
		final = (age + 9)/2
	elif age >= 15: 
		final = (age - 9)/2
	else:
		(random.random + 18)/2
	return final

#your strength based upon the number of your pill
def strength(pill_number):
	if pill_number == 1:
		strength = 100
	elif pill_number == 2:
		strength = 75
	elif pill_number == 3:
		strength = 50 
	elif pill_number == 4:
		strength = 25
	else:
		strength = random.randint(1, 4)
	return strength 

#your defense based upon the number of your pill
def defense(pill_number):
	if pill_number == 1:
		defense = 25
	elif pill_number == 2:
		defense = 50
	elif pill_number == 3:
		defense = 75
	elif pill_number == 4:
		defense = 100
	else:
		defense = random.randint(1, 100)
	return defense

#your weapon will decide if you win of lose. 
#you have to elif everything 
def weapon(weapon_of_choice, strength, defense):
	if weapon_of_choice == "sword & sheild" and strength >= 50 and defense <= 50:
		print "Good job! You have slayed the monster and won!"

	elif not weapon_of_choice == "sword & sheild" and not strength >= 50 and not defense <= 50:
		print "Sorry, you got killed and have lost the game.."

	elif weapon_of_choice == "gun" and strength >= 25 and defense <= 75:
		print "Good job! You have slayed the monster and won!"

	elif not weapon_of_choice == "gun" and not strength >= 25 and not defense <= 75:
		print "Sorry, you got killed and have lost the game.."

	elif weapon_of_choice == "bow & arrow" and strength >= 0 and defense >= 50:
		print "Good job! You have slayed the monster and won!"

	elif not weapon_of_choice == "bow & arrow" and not strength >= 0 and not defense >= 50:
		print "Sorry, you got killed and have lost the game.."

	elif weapon_of_choice == "magical wand":
		print "You have won! How ever since you used the wand you will be" 

def output():
	print """
You are walking along a path in a forest and you come upon a monster.
"""


def main():
	do_you_want_to_fight = raw_input("Do you want to fight with it? (yes/no) ")
	age = raw_input("How old are you? ")
	chose_a_pill = raw_input("Chose a pill, 1, 2, 3, 4 or random. ")
	chose_a_weapon = raw_input("Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand. ")
	your_choice = choice(do_you_want_to_fight)
	your_lives = lives(age)
	your_stregth = strength(chose_a_pill)
	your_defense = defense(chose_a_pill)
	
