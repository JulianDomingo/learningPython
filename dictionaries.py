import sys
import pprint

# For loops don't always have to be bounded by range().

# dictionary = {'Here comes':'dat boi', 'Dicks out':'for harambe'}
# # keys()
# print('Prints keys:')
# for key in dictionary.keys():
# 	print(key)

# # values()
# print('Prints key values:')
# for value in dictionary.values():
# 	print(value)

# # items()
# print('Prints items (key, key value):')
# for items in dictionary.items():
# 	print(items)

# print('Prints items separately. For loop has two variables:')
# for key,value in dictionary.items():
# 	print('Key: ' + key + ' Key value: ' + value)


message = 'The zealous fox jumped over the yappy canine.'
count = {}

for character in message:
	count.setdefault(character, 0)				# if character doesn't exist in count yet, put character in count and set it's value to 0. Otherwise, this statement just returns the number of occurrences.
	count[character] = count[character] + 1		# increment the number of occurrences of character

print(count)
pprint.pprint(count)
# print(pprint.pformat(count)) 					# equivalent to line 35
