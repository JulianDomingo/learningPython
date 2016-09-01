import sys, re

def strip(string):
	newString = re.compile(r'\S+')
	string = newString.search(string).group()
	return string

def strip(string, toStrip):
	stripped = re.compile(toStrip)
	string = stripped.sub('', string)
	return string

while True:
	print('Type string to strip.')
	string = input()
	print('Do you want to specify second argument? (yes/no)')
	response = input()
	if response == 'yes':
		print('Specify characters to strip from string.')
		toStrip = input()
		string = strip(string, toStrip)
		print(string)
	elif response == 'no':
		string = strip(string)
		print(string)
	else:
		print('Invalid input.')
