import sys

tableData = [['apples', 'bananas', 'cherries'],
			 ['Alice', 'Bob', 'Carol'],
			 ['10', '6', '54']]

def printTable(tableData):
	# find largest string in each column
	colWidth = [0]*len(tableData)
	for index1 in range(len(tableData[0])):
		for index2 in range(len(tableData)):
			if len(tableData[index2][index1]) > colWidth[index2]:
				colWidth[index2] = len(tableData[index2][index1])

	for index1 in range(len(tableData[0])):
		for index2 in range(len(tableData)):
			print(tableData[index2][index1].rjust(colWidth[index2]) + ' ', end='')
		print('')

printTable(tableData)
