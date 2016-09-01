import sys

cList = []
listLen = 0
while True:
	print('Enter name, or press enter to stop.')
	name = input()
	if name == '':
		break
	else:
		cList += [name]
		listLen += 1

print('List of names:')
for i in range(0, listLen):
	print(cList[i])
