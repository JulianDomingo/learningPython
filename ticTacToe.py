import sys
import pprint

board = {'TL':' ', 'TM':' ', 'TR':' ',
		 'ML':' ', 'MM':' ', 'MR':' ',
		 'BL':' ', 'BM':' ', 'BR':' '}

notation = {'TL':'Top left', 'TM':'Top mid', 'TR':'Top right',
			'ML':'Middle left', 'MM':'Middle mid', 'MR':'Middle right',
			'BL':'Bottom left', 'BM':'Bottom mid', 'BR':'Bottom right'}

def printBoard():
	print(' ' + board['TL'] + ' ' + '|' + ' ' + board['TM'] + ' ' + '|' + ' ' + board['TR'])
	print('-----------')
	print(' ' + board['ML'] + ' ' + '|' + ' ' + board['MM'] + ' ' + '|' + ' ' + board['MR'])
	print('-----------')
	print(' ' + board['BL'] + ' ' + '|' + ' ' + board['BM'] + ' ' + '|' + ' ' + board['BR'])

def checkBoard(player):
	if ((board['TL'] == player and board['TM'] == player and board['TR'] == player) or
		(board['TL'] == player and board['MM'] == player and board['BR'] == player) or
		(board['TL'] == player and board['ML'] == player and board['BL'] == player) or
		(board['ML'] == player and board['MM'] == player and board['MR'] == player) or
		(board['BL'] == player and board['BM'] == player and board['BR'] == player) or
		(board['TM'] == player and board['MM'] == player and board['BM'] == player) or
		(board['TR'] == player and board['MR'] == player and board['BR'] == player) or
		(board['TR'] == player and board['MM'] == player and board['BL'] == player)):

		if player == 'O':
			print('Player 1 has won!')
			return True
		else:
			print('Player 2 has won!')
			return True
	else:
		return False


print('Welcome to Tic Tac Toe. Type \'O\' for player 1 and '
	  '\'X\' for player 2.')
print('To make a move, type the desired cell\'s key as seen under notation ' \
	  'followed by \'O\' for p1 and \'X\' for p2.')
print('Notation:')
pprint.pprint(notation)

while True:
	printBoard()
	move = input()
	location = move[0:2]
	player = move[2:3]

	if player == 'O':
		#prevPlayer = player
		if board[location] == ' ':
			board[location] = player
		else:
			print('A checker is already here!')

	elif player == 'X':
		#prevPlayer = player
		if board[location] == ' ':
			board[location] = player
		else:
			print('A checker is already here!')
	else:
		print('Invalid input.')

	if checkBoard(player):
		print('Play again? Type "Yes"/"No".')
		if input() == 'Yes':
			# clearBoard()
			continue
		else:
			break
	


