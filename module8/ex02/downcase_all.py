#!/usr/bin/env python3

import sys

def downcase_it(str):
	return(str.lower())

if len(sys.argv) == 1:
	print("none")
	sys.exit()
params = sys.argv[1:]
for val in params:
	print(downcase_it(val))
