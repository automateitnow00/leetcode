#recursion
def factorial(n):
    if n == 0: return 1
    res = n * factorial(n - 1)
    return res

print(factorial(5))

def fact(n):
    i = 1
    while n:
        i *= n
        n -= 1
    return i
print(fact(5))
print(factorial(5) == fact(5))