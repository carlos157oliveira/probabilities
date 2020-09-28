'''
What is the probability of a set of n people having at least a pair that
holds the birthday party in the same day of the year?
'''

import math
import random
import sys

if len(sys.argv) == 4:
	n = int(sys.argv[1])
	days_of_year = int (sys.argv[2])
	count = int(sys.argv[3])
else:
	# number of days in a normal year
	days_of_year = 365

	# number of people
	n = 2

	# number of iterations for the simulation: how much scenarios should be tested?
	# greater number leads to more precise results (and more load to the script)
	count = 10**5

def check_duplicates(elems):
	setOfElems = set()
	for elem in elems:
		if elem in setOfElems:
			return True
		else:
			setOfElems.add(elem)
	return False


print(f'Which is the probability of having two people of a set of n={n}' 
	' people to have birhtdays on the same day?')

# (days_of_year**n - math.perm(days_of_year, n)) / days_of_year**n
theoretical_result = 1 - math.perm(days_of_year, n) / days_of_year**n

print('Theoretical result: {}'.format(theoretical_result))

same_day_birthdays = 0
for i in range(count):
	birthdays = []
	for u in range(n):
		birthdays.append(random.randint(1, days_of_year))
	
	if(check_duplicates(birthdays)):
		same_day_birthdays += 1

print('Simulation: {}'.format(same_day_birthdays / count))
		
 
		



