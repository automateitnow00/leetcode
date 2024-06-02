def reverseBits(n):
    binary = list(bin(n))[2:]
    binary = reversed(["0"] * (32 - len(binary)) + binary)
    #print(len(binary))
    binary = "".join(binary)
    return int(binary, 2)

n = int("00000010100101000001111010011100" , 2)
print(reverseBits(n))