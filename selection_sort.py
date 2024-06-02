def selection_sort(arr):
    res = []
    for i in range(len(arr)):
        x = min(arr)
        arr.remove(x)
        res.append(x)
    return res

nums = [1,43,1,23980980,4,1123,4,12,3]
sorted_nums = selection_sort(nums)
print(sorted_nums)