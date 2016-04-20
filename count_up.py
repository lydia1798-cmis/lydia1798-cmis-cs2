

def count_up(n, x):
	if n >= x + 1:
		print "Explosions everywhere!!!!!!!!! The world is begin taken over by unknown fores. We must evacuate emidiatly and get to the nearest spaceport! Please keep calm and freak out."
	else:
		print n , "yeah!"
		count_up(n + 1, x)


def main():
	n = int(raw_input("Type the number you want to start with: "))
	x = int(raw_input("Type the number you want to finish with: "))
	count_up(n, x)
	return

main()
		
