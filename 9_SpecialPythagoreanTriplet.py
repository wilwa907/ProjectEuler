check = True
while check:
    for a in range(1, 500):
        for b in range(a, 500):
            c = (a*a + b*b)**0.5  # Pythagorean Theorem
            if a + b + c == 1000:
                check = False
                print("a: ", a, ", b: ", b, ", c: ", c)
                print("Which gives the product: ", int(a*b*c))
