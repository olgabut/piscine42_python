#!/usr/bin/env python3

def average(cl):
	if len(cl) == 0:
		return (0)
	sum = 0
	for name in cl:
		if isinstance(cl[name], int) or isinstance(cl[name], float):
			sum += cl[name]
	return(sum / len(cl))


class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8.4,
	"luc": 9
}
class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13,
	# "marek": 11
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
