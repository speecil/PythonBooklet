def factorsOf(n):
    factors = [1]
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

            

num = int(input('number: '))
print(factorsOf(num))