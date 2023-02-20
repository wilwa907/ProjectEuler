import numpy as np
f = open("8_input.txt", "r")  # Open file for reading

lines = f.readlines()
numbers = []
for i in lines:  # Remove "\n" at each line and append to numbers list
    numbers.append(i[:-1])

number = int("".join(numbers))  # Join all strings in list to an integer number

largestNumber = 0
count = 0
for n in range(0, int(len(str(number)))-12):
    fourDigitNumber = []
    fourDigitNumberInt = []

    for i in range(0, 13):
        fourDigitNumber.append(str(number)[count+i])

    fourDigitNumberInt.append(int(fourDigitNumber[0]))
    fourDigitNumberInt.append(int(fourDigitNumber[1]))
    fourDigitNumberInt.append(int(fourDigitNumber[2]))
    fourDigitNumberInt.append(int(fourDigitNumber[3]))
    fourDigitNumberInt.append(int(fourDigitNumber[4]))
    fourDigitNumberInt.append(int(fourDigitNumber[5]))
    fourDigitNumberInt.append(int(fourDigitNumber[6]))
    fourDigitNumberInt.append(int(fourDigitNumber[7]))
    fourDigitNumberInt.append(int(fourDigitNumber[8]))
    fourDigitNumberInt.append(int(fourDigitNumber[9]))
    fourDigitNumberInt.append(int(fourDigitNumber[10]))
    fourDigitNumberInt.append(int(fourDigitNumber[11]))
    fourDigitNumberInt.append(int(fourDigitNumber[12]))
    finalNumber = np.prod(fourDigitNumberInt)

    if finalNumber > largestNumber:
        largestNumber = finalNumber
    count += 1
print(largestNumber)
