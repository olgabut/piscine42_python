#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
	sys.exit()
word = input("What was the parameter? ")
if sys.argv[1] == word:
	print("Good job!")
else:
	print("Nope, sorry...")
