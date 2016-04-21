import math
import random

def choice(desicion):
	if desicion == "yes":
		print "You have chosen to fight..."
	else:
		print "You have chosen not to fight, giving the enemy the upper hand and you are killed."	
		exit()

def lives(age):
	if age <= 14: 
		final = (age + 9)/2
	elif age >= 15: 
		final = (age - 9)/2
	return final

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
		strength = random.randint(1, 100)
	return strength 

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

def weapon(weapon_number, strength, defense):
	if weapon_number == "1" and strength >= 50 and defense <= 50:
		return True

	elif not weapon_number == "1" and not strength >= 50 and not defense <= 50:
		return False

	elif weapon_number == "2" and strength >= 25 and defense <= 75:
		return True

	elif not weapon_number == "2" and not strength >= 25 and not defense <= 75:
		return False

	elif weapon_number == "3" and strength >= 0 and defense >= 50:
		return True

	elif not weapon_number == "3" and not strength >= 0 and not defense >= 50:
		return False

	elif weapon_number == "4":
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

def determine_result(strength, defense, weapon_name):
	if your_weapon == True:
		return "The monster comes at you and since you have a strength of {}, a defense of {} and a {},  you win!".format(strength, defense, weapon_name)
	else: 
		return "The monster comes at you but since you have a strength of {}, a defense of {} and a {}, you die....".format(strength, defense, weapon_name)


def magical_wand(weapon):
	if weapon == "4":
		return "Because you used the easiest weapon, the magical wand, it took all of your energy to kill the monster. You only have 1 year left to live."
	

def play_again(lives):
	if lives > 0:
		print "Try again"
		play(lives)

def incremented_lives(play_again, lives):
	if play_again:
		lives = lives - 1

def play(your_lives):
	print "You are walking along a path in a forest and you come upon a monster."
	do_you_want_to_fight = raw_input("Do you want to fight with it? (yes/no) ")
	your_choice = choice(do_you_want_to_fight)
	print "Get ready..." #don't know if I should include this
	chose_a_pill = raw_input("Chose a pill, 1, 2, 3, 4 or random. ")
	your_strength = strength(chose_a_pill)
	your_defense = defense(chose_a_pill)
	weapon_number = raw_input("""
Chose a weapon: 
Type 1 for: sword & sheild  
2 for: A gun
3 for: bow & arrow 
4 for: magical wand

>>>  """)
	your_weapon = weapon(weapon_number, your_strength, your_defense)
	weaponName = weapon_name(weapon_number)
	print output_last(your_strength, your_defense, weaponName, your_lives)
	result = determine_result(your_strength, your_defense, weaponName)
	print result
	print magical_wand(weapon_number)
	return play_again(your_lives)

def main():
	chose_lives = int(raw_input("How old are you?: "))
	your_lives = lives(chose_lives)
	play(your_lives)
	return

main()

