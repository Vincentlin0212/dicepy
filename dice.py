#! /usr/bin/env python

import random
from special_input import *


print("This program simulates rolling several dice.")
print("The user can choose how many dice are rolled.")

howMany = int_input("How many dice would you like to roll? >")
a = 1
for i in range (howMany):
	while True:
		sides = int_input("How many sides on your die #{}? >".format(a))
	
		if sides <= 2:
			print("Sides can't be smaller than 2, try again.")
			continue
		else:
			break
	number = random.randint(1, sides)
	print("The die shows: {}".format(number))
	a += 1
