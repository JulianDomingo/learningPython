#uses list data type

import sys
import random

list = ['a great opportunity will be presented to you',
        'an important decision will lie ahead',
        'fortune awaits',
        'try again',
        'your future looks bright',
        'your future looks dim',
        'you will have good luck today',
        'you will have bad luck today']

while True:
        print('Press enter to see your fortune.')
        user = input()
        if user == '':
                print(list[random.randint(0, len(list) - 1)])
                break
        else:
            print('Invalid input. Press enter.')


