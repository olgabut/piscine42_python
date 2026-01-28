#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("none")
	sys.exit()
try:
	first_num = int(sys.argv[1])
	second_num = int(sys.argv[2])
	if first_num > second_num:
		print("The first parameter shoud be smaller than the second one.")
		sys.exit()
	arr = [val for val in range(first_num, second_num + 1)]
	print(arr)
except ValueError:
	print("Please enter a valid number.")
