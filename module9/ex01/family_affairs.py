#!/usr/bin/env python3

def find_the_redheads(family):
	red = list(filter(lambda p: family[p] == "red", family))
	return (red)

# def find_the_redheads(family):
# 	for person in family:
# 		if not isinstance(person, str) or not isinstance(family[person], str):
# 			continue
# 		if family[person] == "red":
# 			red.append(person)
# 	return (red)


def main():
	dupont_family = {
		"florian": "red",
		"marie": "blond",
		"virginie": "brunette",
		"david": "red",
		"franck": "red"
		}
	print(find_the_redheads(dupont_family))

if __name__=="__main__":
	main()

