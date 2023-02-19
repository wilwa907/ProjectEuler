def gcd(num1, num2):  # Greatest Common Divisor
    while(num2 != 0):
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1


lcm = 1
for i in range(1, 21):  # Get the Least Common Multiple
    lcm = (i * lcm) / gcd(i, lcm)
print(lcm)
