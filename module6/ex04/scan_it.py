#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("none")
	sys.exit()
word = sys.argv[1]
str = sys.argv[2]
print(str.count(word) or "none")
