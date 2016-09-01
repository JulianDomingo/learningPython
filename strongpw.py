import sys
import re

strong = re.compile(r'([A-Za-z0-9!?]){8,}')
upper = re.compile(r'[A-Z]')
lower = re.compile(r'[a-z]')
num = re.compile(r'[0-9]')

while True:
	print('Enter password.')
	pw = input()
	result = strong.search(pw)					# check length >= 8

	if result == None:
		print("Password isn't long enough.")
	else:
		if (bool(upper.search(result.group())) and bool(lower.search(result.group())) and bool(num.search(result.group()))):
			print('Password is strong enough.')
		else:
			print("Password isn't strong enough.")

	

