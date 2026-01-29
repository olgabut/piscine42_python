#!/usr/bin/env python3

def main():
	try:
		age = int(input("Please tell me your age: "))
		if age < 1 or age > 125:
			print("The value is incorrect.")
			return
		print("You are currently {} years old.".format(age))
		i = 10
		while i <= 30:
			print(f"In {i} years, you'll be {age + i} years old.")
			i += 10

	except ValueError:
		print("Please enter a valid number.")


if __name__=="__main__":
	main()