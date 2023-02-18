def primefactors(num):
    factors = []
    i = 2  # Starts with the smallest prime number
    while i <= num:
        if num % i == 0:  # If dividable with current prime factor
            factors.append(i)
            num //= i
        else:
            i += 1  # If no prime factor is found, check next one
    return factors

print(primefactors(600851475143))
print(max(primefactors(600851475143)))
