#! /usr/bin/env python
import random
from special_input import *

howMany = int_input("How many dice would you like to roll? >")
sides = int_input("How many sides on your die? >")

for i in range (howMany):
	number = random.randint(1, sides)
	print("The die shows: {}".format(number))