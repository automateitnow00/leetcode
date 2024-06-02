def fibonacci(n):
    if n == 0: return 0
    res = [0 ,1]
    if n == 1: return res
    n -= len(res) + 1
    while n:
        new = res[-1] + res[-2]
        res.append(new)
        n -= 1
    return res

print(fibonacci(10))
    