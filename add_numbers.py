#add nmber without using + or -
#this works for positive numbers but fails for negitive numbers
#this works well in java
a = 2
b = 3

a = (bin(a)[2:])
x = 32 - len(a)
a = "0"*x + a
a = list(a)
a.reverse()
b = (bin(b)[2:])
x = 32 - len(b)
b = "0"*x + b
b = list(b)
b.reverse()
i = 0
carry = 0
res = []
while i < 32:
    sum = (int(a[i]) ^ int(b[i]) ^ carry)
    #print(a[i], b[i], carry, sum)
    res.append(str(sum))
    #print(res)
    carry = (int(a[i]) & int(b[i])) | (int(b[i]) & carry) | (carry & int(a[i]))
    i += 1
    
res.reverse()
res = "".join(res)
X = int(res, 2)
print(X)
