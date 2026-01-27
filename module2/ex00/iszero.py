#!/usr/bin/env python3

# chmod + <file_name>

num = input()
try:
	if int(num) == 0:
		print("This number is equal to zero.")
	else:
		print("This number is different from zero.")
except ValueError:
	print("Please enter a valid number.")