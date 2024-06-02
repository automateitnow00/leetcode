def armstrong(n):
    if n < 10 and n != 1: return False
    n = str(n)
    length = len(n)
    res = 0
    for i in n: res += int(i)**length
    return (res == int(n))

armstrong_numbers = [1, 370, 9, 371, 1634, 8208, 9474]
result = [armstrong(i) for i in armstrong_numbers]
print(result)
