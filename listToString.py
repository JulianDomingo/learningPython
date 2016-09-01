import sys

userList = []
userString = ''

def stringConv(userList):
	global userString
	for index in range(0, len(userList)):
		if index == (len(userList) - 1):
			userString = userString + 'and ' + userList[index]
		else:
			userString = userString + userList[index] + ', '


print('Enter your list. Type "quit" to end list.')

while True:
	item = input()
	if item != 'quit':
		userList.append(item)
	else:
		break

stringConv(userList)
print(userString)
