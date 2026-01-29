#!/usr/bin/env python3

def array_of_names(persons):
	result = list()
	for item in persons:
		if not isinstance(item, str) or not isinstance(persons[item], str):
			continue
		result.append((str(item).capitalize() + ' ' + str(persons[item]).capitalize()))
	return(result)


persons = {
"jean": "valjean",
"grace": "hopper",
2.4: 7.5,
"xavier": "niel",
"fifi": "brindacier",
0: 1,
(1, 2): ["hi", "ahoj"]
}

print(array_of_names(persons))
