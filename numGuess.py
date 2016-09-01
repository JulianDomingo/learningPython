import random

print('Thinking of a number between 1 and 15 inclusive.')
# For a specific number, numToGuess = 15
# For a random numer,
numToGuess = random.randint(1, 16)
while True:
	print('What is your guess?')
	guess = input()
	if int(guess) > 15:
		print('Invalid input.')
		continue
	elif int(guess) == numToGuess:
		print('You correctly guessed the number ' + str(numToGuess) + '.')
		print('Good job!')
		break
	elif int(guess) < numToGuess:
		print('Your guess is too low.')
	elif int(guess) > numToGuess:
		print('Your guess it too high.')

