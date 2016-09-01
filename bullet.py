import sys, pyperclip

text = pyperclip.paste()								# assumes the clipboard contains the text to be bulleted

lines = text.split('\n')
for index in range(len(lines)):
	lines[index] = '* ' + lines[index]

text = '\n'.join(lines)
pyperclip.copy(text)
