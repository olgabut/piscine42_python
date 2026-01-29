#!/usr/bin/env python3

try:
	user_say = input("What you gotta say? : ")

	while user_say != "STOP":
		try:
			user_say = input("I got that! Anything else? : ")
		except KeyboardInterrupt:
			print("\nERROR")

except KeyboardInterrupt:
	print("\nERROR")
