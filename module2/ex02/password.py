#!/usr/bin/env python3

# from getpass import getpass
# userpass = getpass()

userpass = input()

password = "Python is awesome"
if password == userpass:
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")