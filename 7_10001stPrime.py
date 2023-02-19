primes = [2, 3]
i = 3
while len(primes) != 10001:
    i += 1
    check = True
    for j in range(2, i-1):
        if (i % j) == 0:  # Check if dividable with something expect 1 and itself
            check = False
            break
    if check:  # If prime
        primes.append(i)
print(primes[-1])
