#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
	sys.exit()
print("parameters: ", len(sys.argv) - 1)
for i, param in enumerate(sys.argv):
	if i > 0:
		print(param + ':',  len(param))
