"""You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise."""

flowerbed = [0,0,1]
def canPlaceFlowers(flowerbed, n: int) -> bool:
    flowerbed.insert(0,0)
    flowerbed.append(0)
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1

    return (n <= 0)

X = canPlaceFlowers(flowerbed, 1)
print(X)