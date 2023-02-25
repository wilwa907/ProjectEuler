# (n + n)!/(n! * n!)
def factorial(n):  # Calculate the factorial
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result


def count_paths(n):  # Count the number of paths
    numerator = factorial(n+n)
    denominator = factorial(n)
    return int(numerator/(denominator*denominator))


n = 20
print("Paths:", count_paths(n))