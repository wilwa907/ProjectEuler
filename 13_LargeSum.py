file = open("13_input.txt", "r")
lines = file.readlines()

number = []
for i in lines:  # Remove "\n" at each line and append to number
    number.append(i[:-1])

number2 = []
for i in range(0, len(number)):  # Create a 2D grid of string values
    number2.append(number[i].split(' '))

sumOfNum = 0
for i in range(0, len(number2)):
    sumOfNum += int(number2[i][0])

print(sumOfNum)
num = int(str(sumOfNum)[:10])
print(num)
