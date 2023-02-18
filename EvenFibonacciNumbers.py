fib = [1, 2]
while fib[-1] < 4000000:  # Stop when exceeding 4 000 000, but will include last element > 4 000 000
    fib.append(fib[-1] + fib[-2])  # Sum of the two last numbers in fib list

fib = fib[0:-1]  # exclude last element

fibEven = []
# Loop through all the Fibonacci numbers and get all the even once
for i in fib:
    if i % 2 == 0:
        fibEven.append(i)
print(fibEven)
print(sum(fibEven))
