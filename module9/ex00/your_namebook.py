#!/usr/bin/env python3

def array_of_names(persons):
	result = []
	for item in persons:
		if not isinstance(item, str) or not isinstance(persons[item], str):
			print("ERROR: The dictionary contains wrong data.")
			return
		print(str(item).capitalize() + ' ' + str(persons[item]).capitalize())

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier",
0: 1,
2.4: 7.5,
(1, 2): ["hi", "ahoj"]
}

array_of_names(persons)
