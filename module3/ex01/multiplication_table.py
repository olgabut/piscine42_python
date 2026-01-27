#!/usr/bin/env python3

try:
	print("Enter a number")
	num = int(input())

	i = 0
	while i < 10:
		print(i, 'x', num, '=', i * num)
		i += 1

except ValueError:
	print("Please enter a valid number.")