def isprime(x):
    check = True
    for n in range(2, int(x**0.5+1)):  # Only need to check numbers up to the square root
        if x % n == 0:
            check = False
            break
    return check

sum = 2
for i in range(3, 2000000):
    if isprime(i):
        sum += i
print(sum)


