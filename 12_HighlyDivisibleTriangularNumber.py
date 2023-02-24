check = True
numbers = [1]
sums = 1

while check:
    divisors = 0
    for i in range(1, int(sums**0.5)+1):  # Only need to check numbers up to the square
        if sums % i == 0:                 # root and then adding 2 divisors att line 9
            divisors += 2
    if divisors > 500:
        print("Number:", sums)
        check = False
    numbers.append(numbers[-1] + 1)
    sums += numbers[-1]
