def primenums(n):
    if n == 0 or n == 1: return 0
    primes = [True] * n
    primes[0], primes[1] = False, False
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n , p):
                primes[i] = False
        p += 1
    return primes.count(True)

print(primenums(100))