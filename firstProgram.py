print('Hello, user.')
print('What is your name?')
name = input()
print('Welcome, ' + name)
print('Your name is ')
print(len(name))
print(' letters long.')
print('What about your age?')
age = input()
ageVal = int(age)
print('You are ' + age + ' years old.')
if ageVal >= 21:
	print('You are old enough to legally drink in the U.S.')
else:
	print('You cannot legally drink in the U.S.')
	if ageVal == 20:
		print('Just one more year to go, though!')
