import random

# Returns a random number between 1 and 6
def roll(num_dice):
	dice_nums = [random.randint(1,6) for x in range(num_dice)]

	return dice_nums

while True:
	# Ask user if they would like to roll
	choice = input("Would you like to roll? (yes or no)\n")

	if choice.strip().lower() == 'yes':
		num_dice = int(input("How many dice would you like to roll?\n"))
		# Roll dice
		dice = roll(num_dice)
		# print number on die
		for die in dice:
			print("You rolled a " + str(die))
	elif choice.strip().lower() == 'no':
		print("Thanks for rolling!")
		break
	else:
		print("I am not sure I understand what you are asking. Try again.")
