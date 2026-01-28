#!/usr/bin/env python3


try:
	num = float(input("Give me a number: "))
	if num.is_integer():
		print(int(num))
	else:
		if num < 0:
			print(int(num))
		else:
			print(int(num) + 1)

except ValueError:
	print("Please enter a valid number.")
