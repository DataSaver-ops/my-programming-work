def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


print(factors(15))
