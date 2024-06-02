def replaceElements(arr):
    res = []
    res.append(-1)
    maximum = float("-inf")
    i = -1
    while i > -len(arr):
        maximum = max(maximum, arr[i])
        res.insert(0, maximum)
        i -= 1

    return res

nums = [1,2,3,4]
print(replaceElements(nums))
