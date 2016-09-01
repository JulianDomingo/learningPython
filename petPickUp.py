import sys

petList = ['Snowball', 'Lily', 'Fluffy', 'Jack', 'Max']

def inCare(petName):
	if petName in petList:
		return True
	else:
		return False

print('Welcome to the pet day care. What is the name of your pet?')
petName = input()
if inCare(petName):
	print('Ah yes, hello ' + petName + '\'s' + ' owner. We will get ' + petName + ' right away.')
else:
	print(petName + ' isn\'t here right now. Are you sure you\'re at the right day care?')
