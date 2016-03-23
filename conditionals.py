# My script will be of a fight. You are walking along a path in the forest when you come upon a monster. "Do you want to fight with it?" If you say yes then you will keep playing if you say no then the moster will kill you. If you say yes, then you have to get ready to fight. The first question that you will be asked is "How old are you?" If you are from 1-14 then you get 9 lives added and one extra life by how far away from zero you are. If you are 14+ then you get 9 lives subtracted and a life added by how far away from zero you are. The second question that you will be asked is "Chose a pill, 1, 2, 3, 4 or a wild card." If you chose #1 = 100 strengths + 25 defenses. #2 = 75 strengths + 50 defenses. #3 = 50 stregths + 75 defenses. #4 = 25 strengths + 100 defenses. If you chose wild it will take a random number from 1-100 for each defense and strength. Next you will be asked "Chose a weapon: sword & sheild, a gun, a bow & arrow and a magical wand." Sword & sheild = If strength is more than 50 & defense is less than 50 then you win. If not you lose. Gun = If strenght is more than 25 and defense is less than 75 then you win. Bow and arrow = If strength is more than 0 and defense is more than 50 then you win. Magical wand = you always win but you will be teleported anywhere in the world. Then you will 'fight' with the monster and you will either win (you live) or you lose (you die).

import random

def lives(age):
	if age <= 14 
		final = age + 9 + age/2
	elif age >= 15 
		final = age - 9 + age/2
	return final

def stregth(pill_number):
	if pill_number == 1 
		strength = 100
	elif pill_number == 2
		strength = 75
	elif pill_number == 3
		strength = 50 
	elif pill_number == 4
		strength = 25
	else:
		strength = random.randint(1, 100)
	return strength 

def defense(pill_number):
	if pill_number == 1
		defense = 25
	elif pill_number == 2
		defense = 50
	elif pill_number == 3
		defense = 75
	elif pill_number == 4
		defense = 100
	else:
		defense = random.randint(1, 100)
	return defense

