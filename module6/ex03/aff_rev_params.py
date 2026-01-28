#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
else:
	arr = [value for i, value in enumerate(sys.argv) if i > 0]
	arr = list(reversed(arr))
	for value in arr:
		print(value)
