#!/usr/bin/env python3

try:
	age = int(input("Please tell me your age: "))
	print("You are currently %s years old." % age)
	i = 10
	while i <= 30:
		print("In {} years, you'll be {} years old.".format(i, age + i))
		i += 10

except ValueError:
	print("Please enter a valid number.")
