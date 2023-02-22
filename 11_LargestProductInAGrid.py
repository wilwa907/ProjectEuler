import numpy as np
file = open("11_input.txt", "r")  # Open file for reading
largestProduct = 0
lines = file.readlines()

grid = []
for i in lines:  # Remove "\n" at each line and append to grid
    grid.append(i[:-1])

grid2D = []
for i in range(0, len(grid)):  # Create a 2D grid of string values
    grid2D.append(grid[i].split(' '))

# Find the largest horizontal product
for hline in range(0, 20):
    horizontalCount = 0
    for i in range(0, int(len(grid2D[0]))-3):
        fourDigit = []
        fourDigitInt = []
        for j in range(0, 4):
            if grid2D[hline][horizontalCount + j].startswith("0"):
                grid2D[hline][horizontalCount + j].replace('0', '')
            fourDigit.append(grid2D[hline][horizontalCount + j])
        fourDigitInt.append(int(fourDigit[0]))
        fourDigitInt.append(int(fourDigit[1]))
        fourDigitInt.append(int(fourDigit[2]))
        fourDigitInt.append(int(fourDigit[3]))
        product = np.prod(fourDigitInt)
        if product > largestProduct:
            largestProduct = product
        horizontalCount += 1

# Find the largest vertical product
for vline in range(0, 20):
    column = [row[vline] for row in grid2D]
    verticalCount = 0
    for i in range(0, int(len(grid2D[0]))-3):
        fourDigit = []
        fourDigitInt = []
        for j in range(0, 4):
            if column[verticalCount + j].startswith("0"):
                column[verticalCount + j].replace('0', '')
            fourDigit.append(column[verticalCount + j])
        fourDigitInt.append(int(fourDigit[0]))
        fourDigitInt.append(int(fourDigit[1]))
        fourDigitInt.append(int(fourDigit[2]))
        fourDigitInt.append(int(fourDigit[3]))
        product = np.prod(fourDigitInt)
        if product > largestProduct:
            largestProduct = product
        verticalCount += 1

# Find the largest left-to-right diagonal product
for dline1 in range(0, int(len(grid2D[0]))-3):
    diagonalCount1 = 0
    for i in range(0, int(len(grid2D[0]))-3):
        fourDigit = []
        fourDigitInt = []
        for j in range(0, 4):
            if grid2D[dline1 + j][diagonalCount1 + j].startswith("0"):
                grid2D[dline1 + j][diagonalCount1 + j].replace('0', '')
            fourDigit.append(grid2D[dline1 + j][diagonalCount1 + j])
        fourDigitInt.append(int(fourDigit[0]))
        fourDigitInt.append(int(fourDigit[1]))
        fourDigitInt.append(int(fourDigit[2]))
        fourDigitInt.append(int(fourDigit[3]))
        product = np.prod(fourDigitInt)
        if product > largestProduct:
            largestProduct = product
        diagonalCount1 += 1

# Find the largest right-to-left diagonal product
for dline2 in range(0, int(len(grid2D[0]))-3):
    diagonalCount2 = 19
    for i in range(19, int(len(grid2D[0]))-18, -1):
        fourDigit = []
        fourDigitInt = []
        for j in range(0, 4):
            if grid2D[dline2 + j][diagonalCount2 - j].startswith("0"):
                grid2D[dline2 + j][diagonalCount2 - j].replace('0', '')
            fourDigit.append(grid2D[dline2 + j][diagonalCount2 - j])
        fourDigitInt.append(int(fourDigit[0]))
        fourDigitInt.append(int(fourDigit[1]))
        fourDigitInt.append(int(fourDigit[2]))
        fourDigitInt.append(int(fourDigit[3]))
        product = np.prod(fourDigitInt)
        if product > largestProduct:
            largestProduct = product
        diagonalCount2 -= 1
print("Largest product:", largestProduct)
