palindromes = []
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i*j  # Create to identical numbers since one is later modified when creating the reversed number
        num2 = i*j
        # Create a reversed number
        reversedNum = 0
        while num != 0:
            digit = num % 10
            reversedNum = reversedNum*10 + digit
            num //= 10  # num will be rounded to the closest int

        if num2 == reversedNum:
            palindromes.append(num2)
print(max(palindromes))