# In python, 'def' functions do not have to have the same return type. However, methods must have identical return values.
# I will most likely learn this later on in this book.

import sys

def returnIt(val):
	if val > 0:
		return 0
	elif val < 0:
		return True
	elif val == 0:
		return 'hi'

print('Type an int value.')
rVal = input()
printThis = returnIt(int(rVal))
print(printThis)
