#! python3
# Detects all e-mails and phone numbers in clipboard text.

import sys, re, pyperclip

phone = re.compile(r'''
	(\d{3}|\(\d{3}\))											# area code
	([- ])?													# optional separator
	(\d{3})													# phone number part 1
	([- ])?													# optional separator
	(\d{4})													# phone number part 2
''', re.VERBOSE | re.DOTALL)

email = re.compile(r'''(
	[a-zA-Z0-9\.]+												# email must be at least one character
	@													# must have this to be an email
    [a-zA-Z0-9]+												# domain name
	\.[a-zA-Z]{2,4}												# email must end with one of these options
)''', re.VERBOSE)


text = pyperclip.paste()
print("Type 'phone' for phone numers or 'email' for emails. Press 'q' to quit.")
while True:
	choice = input()

	if choice.lower() == 'phone':
		numbers = phone.findall(text)
		for index in range(0, len(numbers)):
			numbers[index] = ''.join(numbers[index])						# joins together the strings in each tuple in the list of tuples
		pyperclip.copy('\n'.join(numbers))								# joins together each index of list with a newline
		print('Copied all phone numbers. Press any key to exit.')
		sys.exit()

	elif choice.lower() == 'email':
		emails = email.findall(text)
		for index in range(0, len(emails)):
			emails[index] = ''.join(emails[index])
		pyperclip.copy('\n'.join(emails))
		print('Copied all emails. Press any key to exit.')
		sys.exit()

	elif choice.lower() == 'q':
		sys.exit()

	else:
		print("Invalid Input.")
		continue
