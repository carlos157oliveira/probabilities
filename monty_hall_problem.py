'''
You might read more here: https://en.wikipedia.org/wiki/Monty_Hall_problem
Lets simulate!
'''

import random

# how many times the result was in favor of the player?
wins = 0
# total number of simulation iterations
count = 10**5
# quantity of doors
n = 3

for _ in range(count):

	opened = [False] * n
	prize = [False] * n

	prize[random.randint(0, n - 1)] = True
	user_choice = random.randint(0, n - 1)
	
	# opens randomly a door that doesn't contain the prize and hasn't been chosen
	doors_to_open = [i for i in range(n) if not prize[i] and i != user_choice]
	opened[random.choice(doors_to_open)] = True

	# In our simulation, the player always switches the door
	# He picks another door from what he chose
	# This new chosen door isn't opened yet
	for i in range(n):
		if i != user_choice and not opened[i]:
			user_choice = i
			# after the choice has been made, break so that it isn't reversed
			break

	if prize[user_choice]:
		wins += 1

print(f'Switching doors, the player gained {wins / count * 100}% of the times.')
