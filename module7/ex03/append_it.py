#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
	sys.exit()
for val in sys.argv[1:]:
	if len(val) < 3 or val.find("ism", len(val) - 3) != (len(val) - 3):
		print(val + "ism")

#print("".join([val+"ism\n" for val in enumerate(sys.argv[1:]) if not val.endswith("ism")])[:-1])
#[val+"ism\n" for i, val in enumerate(sys.argv) if i > 0 and not val.endswith("ism")]