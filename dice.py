#! /usr/bin/env python

import random
from special_input import *

howMany = int_input("How many dice would you like to roll? >")
a = 1
for i in range (howMany):
	
	sides = int_input("How many sides on your die #{}? >".format(a))
	number = random.randint(1, sides)
	print("The die shows: {}".format(number))
	a += 1