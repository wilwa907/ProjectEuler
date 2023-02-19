squaresOfSum = []  # (1 + 2 + 3)^2
sumOfSquare = []  # (1^2 + 2^2 + 3^2)
for i in range(1, 101):
    squaresOfSum.append(i)
    sumOfSquare.append(i**2)

sum1 = sum(squaresOfSum)**2
sum2 = sum(sumOfSquare)
diff = sum1-sum2
print(diff)