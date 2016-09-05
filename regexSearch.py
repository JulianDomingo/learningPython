#! python3
# opens all .txt files in a folder (specified by user) and
# searches for any line that matches a regex (also specified
# by user)

import os, re

txtFinder = re.compile(r'[A-Za-z0-9_]+\.txt')									# regex to find all .txt files in a directory

print('Enter directory location of .txt files:')
os.chdir(input())
txtFiles = txtFinder.findall(', '.join(os.listdir()))							# finds all .txt files and stores in list

print('Enter regular expression for searching .txt files:')
print("Format: <expression>")
userRegex = re.compile(input())													# create user-specified regex

print(os.listdir())

for file in txtFiles:
	content = open(file, 'r')
	print(', '.join(userRegex.findall(content.read())))									# find all occurrences and convert to str before output to console

