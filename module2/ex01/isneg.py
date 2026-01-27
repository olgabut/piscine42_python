#!/usr/bin/env python3

try:
	num = float(input())
	if num < 0:
		print("This number is negative.")
	elif num > 0:
		print("This number is positive.")
	else:
		print("This number is both positive and negative.")
except ValueError:
	print("Please enter a valid number.")