#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
	print("none")
	sys.exit()
print("".join([char for char in sys.argv[1] if char == 'z']) or "none")

# count = sys.argv[1].count('z')
# if count == 0:
# 	print("none")
# else:
# 	for _ in range(count):
# 		print('z', end='')
# 	print()
