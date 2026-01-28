#!/usr/bin/env python3

import sys

def shrink(s):
	print(str(s)[:8])

def enlarge(s):
	s = str(s)
	while len(s) < 8:
		s += 'Z'
	print(s)

if len(sys.argv) == 1:
	print("none")
	sys.exit()
params = sys.argv[1:]
for val in params:
	if len(val) > 8:
		shrink(val)
	else:
		enlarge(val)
