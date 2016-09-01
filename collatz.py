import sys

def collatz(strNum):
	try:
		num = int(strNum)
	except:
		print('Invalid input. Enter an integer next time.')
	while num != 1:
		if int(num)%2 == 0:															# even
			num /= 2
		elif int(num)%2 == 1:
			num = (3 * num) + 1
		else:
			break
		print(int(num))
	return num

print('Enter a number:')
userInput = input()
collatz(userInput)
