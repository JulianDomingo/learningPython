#! python 3

''' Generates a specified amount of quizzes/answer key text files testing whether 
    an individual knows states and thier corresponding capitals. 
'''

import random, sys, shelve

answerKey = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock',
			 'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover',
			 'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise',
			 'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka',
			 'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis',
			 'Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'St. Paul', 'Mississippi':'Jackson',
			 'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 
			 'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 'New York':'Albany', 
			 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City', 
			 'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 
			 'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City',
			 'Vermont':'Montpelier', 'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston',
			 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

letterChoices = ['A', 'B', 'C', 'D']

# Create 35 quiz files and corresponding answer keys.
for numQuiz in range(35):

	quiz = open('quiz' + str(numQuiz + 1) + '.txt', 'w')									# creates new file "quizX.txt" where X is range(35) + 1.
	key = open('quiz' + str(numQuiz + 1) + '_ans.txt', 'w')									# creates corresponding answer key text file.

	# Create header and title for the quiz / answer key.
	quiz.write('Name:\nDate:\n' + ('\n' * 2))
	quiz.write((' ' * 20) + 'States and their Capitals Quiz ' + str(numQuiz + 1) + (' ' * 20) + ('\n' * 3))
	key.write((' ' * 20) + 'States and their Capitals Quiz ' + 'Answer Key # ' + str(numQuiz + 1) + ('\n' * 2))

	# Randomly shuffle order of states to ask.
	states = list(answerKey.keys())												# list of capitals
	random.shuffle(states)

	# Write the questions and corresponding answers into the text file
	for question in range(50):
		
		quiz.write(str(question + 1) + '. What is the Capital of ' + states[question] + '?\n')
		key.write(str(question + 1) + '. ' + answerKey[states[question]] + '\n')
		ans = letterChoices[random.randint(0, 3)]
		
		for choice in letterChoices:
			if choice == ans:
				quiz.write((' ' * 4) + ans + '. ' + answerKey[states[question]] + '\n')				# print right answer
			else:
				while True:											# print randomized wrong answer
					notAns = random.randint(0, 49)
					if notAns != question:
						break
				quiz.write((' ' * 4) + choice + '. ' + answerKey[states[notAns]] + '\n')
		quiz.write('\n')

	quiz.close()
	key.close()


