import sys

words = 'The lazy cat jumped over the zealous fox.'.split()
list = [[w.upper(), w.lower(), len(w)] for w in words]

for index in list:
	print(index)
