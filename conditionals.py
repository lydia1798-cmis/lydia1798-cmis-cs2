# My script will be of a fight. You are walking along a path in the forest when you come upon a monster. "Do you want to fight with it?" If you say yes then you will keep playing if you say no then the moster will kill you. If you say yes, then you have to get ready to fight. The first question that you will be asked is "How old are you?" If you are from 1-14 then you get 9 lives added and one extra life by how far away from zero you are. If you are 14+ then you get 9 lives subtracted and a life added by how far away from zero you are. The second question that you will be asked is "Chose a pill, 1, 2, 3, 4 or a wild card." If you chose #1 = 100 strengths + 25 defenses. #2 = 75 strengths + 50 defenses. #3 = 50 stregths + 75 defenses. #4 = 25 strengths + 100 defenses. If you chose random it will take a random number from 1-100 for each defense and strength. Next you will be asked "Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand." Sword & sheild = If strength is more than 50 & defense is less than 50 then you win. If not you lose. Gun = If strenght is more than 25 and defense is less than 75 then you win. Bow and arrow = If strength is more than 0 and defense is more than 50 then you win. Magical wand = you always win but you will be teleported anywhere in the world. Then you will 'fight' with the monster and you will either win (you live) or you lose (you die).

#The questions that are going to be asked:
#	1. "Do you want to fight with it?" (yes, no)
#	3. "Chose a pill, 1, 2, 3, 4 or random." (1, 2, 3, 4, random)
#	4. "Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand." (sword & sheild, a gun, a bow & arrow and a magical wand)

#The story line:
#	"You are walking along a path in a forest and you come upon a monster. (Q.1) 'Do you want to fight it?' (yes, no)
#	No: You have chosen not to fight. Unfortuantly this has made it easier for the monster to kill you and you have just died.
#	Yes: "Get ready to fight....."
#		(Q.3) 'Chose a pill, 1, 2, 3, 4 or random' (1, 2, 3, 4 or random) - If you chose #1 = 100 strengths + 25 defenses. #2 = 75 strengths + 50 defenses. #3 = 50 stregths + 75 defenses. #4 = 25 strengths + 100 defenses. If you chose random it will take a random number from 1-100 for each defense and strength.
#		(Q.4) 'Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand." (sword & sheild, a gun, a bow & arrow and a magical wand) - 
# Sword & sheild = If strength is more than 50 & defense is less than 50 then you win. If not you lose.
# Gun = If strenght is more than 25 and defense is less than 75 then you win.
# Bow and arrow = If strength is more than 0 and defense is more than 50 then you win.
# Magical wand = you always win but you will be teleported anywhere in the world.
#	"Your strength is at {}.
#	"Your defense is at {}.
#	"You have a {}.
#
#	"The monster comes at you and since you have *weapon* you win!
#								OR
#	"The monster comes at you but since you have *weapon* you lose....

import math
import random

def choice(desicion):
	if desicion == "yes":
		print """
You have chosen to fight..."""
	else:
		print """
You have chosen not to fight, giving the enemy the upper hand and you are killed."""	
		exit()

def lives(age):
	if age <= 14: 
		final = (age + 9)/2 
	elif age >= 15: 
		almost_final = (age - 9)/2 
		random_ = random.random
		final = almost_final * random_
	return final

def strength(chose_a_number):
	if chose_a_number == 1:
		strength = 100
	elif chose_a_number == 2:
		strength = 75
	elif chose_a_number == 3:
		strength = 50 
	elif chose_a_number == 4:
		strength = 25
	else:
		strength = random.randint(1, 100)
	return strength 

def defense(chose_a_number):
	if chose_a_number == 1:
		defense = 25
	elif chose_a_number == 2:
		defense = 50
	elif chose_a_number == 3:
		defense = 75
	elif chose_a_number == 4:
		defense = 100
	else:
		defense = random.randint(1, 100)
	return defense

def weapon(weapon_number, strength, defense):
	if weapon_number == 1 and strength >= 50 and defense <= 50:
		return True

	elif not weapon_number == 1 and not strength >= 50 and not defense <= 50:
		return False

	elif weapon_number == 2 and strength >= 25 and defense <= 75:
		return True

	elif not weapon_number == 2 and not strength >= 25 and not defense <= 75:
		return False

	elif weapon_number == 3 and strength >= 0 and defense >= 50:
		return True

	elif not weapon_number == 3 and not strength >= 0 and not defense >= 50:
		return False

	else:
		return True

def weapon_name(weapon_number):
	if weapon_number == 1:
		return "sword and sheild"
	elif weapon_number == 2:
		return "gun"
	elif weapon_number == 3:
		return "bow and arrow"
	elif weapon_number == 4:
		return "magical wand"

def output_last(strength, defense, weapon_name, your_lives):
	life = "lives"
	if lives == 1:
		life = "life"
	return """
You have {} {}.
Your strength is at {}.
Your defense is at {}.
You have a {}.
""".format(your_lives, life, strength, defense, weapon_name)

def determine_result(strength, defense, weapon_name, your_weapon):
	if your_weapon == True:
		return "The monster comes at you and since you have a strength of {}, a defense of {} and a {},  you win!".format(strength, defense, weapon_name)
	else: 
		return """The monster comes at you but since you have a strength of {}, a defense of {} and a {}, you die....
""".format(strength, defense, weapon_name)


def magical_wand(weapon_number):
	if weapon_number == 4:
		return "Because you used the easiest weapon, the magical wand, it took all of your energy to kill the monster. You only have 1 year left to live."
	else:
		return "Because you didn't use the easiest weapon, you are safe from the evil magcial powers of the forest."

def play_again(lives):
	if lives > 0:
		print """
Try again"""
		lives = lives - 1
		return play(lives)

def play(your_lives):
	print """
You are walking along a path in a forest and you come upon a monster.
"""
	do_you_want_to_fight = raw_input("Do you want to fight with it? (yes/no) >>> ")
	your_choice = choice(do_you_want_to_fight)
	print """
Get ready...
""" #don't know if I should include this
	chose_a_number = raw_input("""Chose a number, 1, 2, 3 or 4 >>> """)
	your_strength = strength(chose_a_number)
	your_defense = defense(chose_a_number)
	weapon_number = int(raw_input("""
Chose a weapon: 
Type 1 for: sword & sheild  
2 for: A gun
3 for: bow & arrow 
4 for: magical wand

>>>  """))
	your_weapon = weapon(weapon_number, your_strength, your_defense)
	weaponName = weapon_name(weapon_number)
	print output_last(your_strength, your_defense, weaponName, your_lives)
	print determine_result(your_strength, your_defense, weaponName, your_weapon)
	print magical_wand(weapon_number)
	return play_again(your_lives)

def main():
	chose_lives = int(raw_input("How old are you? >>> "))
	your_lives = lives(chose_lives)
	play(your_lives)
	return
main()

