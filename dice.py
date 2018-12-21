import random
# Random number between 1 and 6 inclusive

while True:
	# Ask user if they would like to roll
	choice = input("Would you like to roll? (yes or no)\n")

	if choice.strip().lower() == 'yes':
		rand_num = random.randint(1, 6)
		# print number on die
		print(rand_num)
	elif choice.strip().lower() == 'no':
		print("Thanks for rolling!")
		break
	else:
		print("I am not sure I understand what you are asking. Try again.")
