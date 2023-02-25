largestCount = 0

for i in range(2, 1000000):
    number = i
    count = 0
    
    while number != 1:
        count += 1
        if number % 2 == 0:
            number /= 2
        elif number % 2 != 0:
            number = 3*number + 1

    if count > largestCount:
        largestCount = count
        num = i

print("Longest sequences obtained for starting number:", num,)
