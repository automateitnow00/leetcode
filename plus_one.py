"""You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""

def plusOne(digits):
    num = ""
    for i in digits:
        num += str(i)
    num = list(str(int(num) + 1))
    num = [int(i) for i in num]
    return num

digits = [9]
print(plusOne(digits))