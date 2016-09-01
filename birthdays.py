import sys

birthdays = {'Snowball':'June 2', 'Lily':'December 5'}

while True:
	print('Type a pet name to see their birthday (Press enter to quit).')
	name = input()

	if name == '':
		break
	elif name in birthdays:
		print(birthdays[name])
	else:
		print('No record of ' + name + '.')
		print('Would you like to add ' + name + ' to the dictionary? (Type "Yes"/"No")')
		response = input()
		if response == 'Yes':
			print('What is their birthday?')
			birthdays[name] = input()
			print('Okay, we\'ve added their birthday.')
		if response == 'No':
			continue

