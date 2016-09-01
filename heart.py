import sys

grid = [['.', '.', '.', '.', '.', '.'],        
		['.', 'O', 'O', '.', '.', '.'],        
		['O', 'O', 'O', 'O', '.', '.'],        
		['O', 'O', 'O', 'O', 'O', '.'],        
		['.', 'O', 'O', 'O', 'O', 'O'],        
		['O', 'O', 'O', 'O', 'O', '.'],        
		['O', 'O', 'O', 'O', '.', '.'],        
		['.', 'O', 'O', '.', '.', '.'],        
		['.', '.', '.', '.', '.', '.']]

def rotateGrid90ToRight(grid):
	
	# initialize 2D list
	newGrid = []
	temp = []
	for x in range(0, len(grid[0])):
		for y in range(0, len(grid)):
			temp.append('')								# make inner list
		newGrid.append(temp)							# insert inner list into index of outer list
		temp = []										# clear temp for next inner list

	for x in range(0, len(grid[0])):					# number of columns
		for y in range(0, len(grid)):					# number of rows
			newGrid[x][y] = grid[y][x]					# put the xth element from the yth row into newGrid

# print the new grid

	for index in range(0, len(newGrid)):				# no double loop, since each index of newGrid prints the whole row
		print(newGrid[index])

rotateGrid90ToRight(grid)

