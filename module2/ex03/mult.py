#!/usr/bin/env python3

try:
	print("Enter the first number:")
	first_num = int(input())
	print("Enter the second number:")
	second_num = int(input())

	mult = first_num * second_num
	print(first_num, 'x', second_num, '=', mult)
	if mult < 0:
		print("The result is negative.")
	elif mult > 0:
		print("The result is positive.")
	else:
		print("The result is positive and negative.")

except ValueError:
	print("Please enter a valid number.")