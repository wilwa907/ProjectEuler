multiples = []
numbers = list(range(1, 1000))

for i in numbers:
    if i % 3 == 0 or i % 5 == 0:  # If number is dividable by 3 or 5
        multiples.append(i)
print(multiples)
print(sum(multiples))
