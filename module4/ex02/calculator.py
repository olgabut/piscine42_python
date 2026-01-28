#!/usr/bin/env python3

try:
	first_num = int(input("Give me the first number: "))
	second_num = int(input("Give me the second number: "))

	print(first_num, '+', second_num, '=', first_num + second_num)
	print(first_num, '-', second_num, '=', first_num - second_num)
	if first_num % second_num == 0:
		print(first_num, '/', second_num, '=', round(first_num / second_num))
	else:
		print(first_num, '/', second_num, '=', first_num / second_num)
	print(first_num, '*', second_num, '=', first_num * second_num)

except ValueError:
	print("Please enter a valid number.")