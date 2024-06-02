def insertion_sort(arr):
    res = []
    for i in arr:
        if (len(res) == 0):
            res.append(i)
        else:
            if i > res[-1]:
                res.append(i)
            elif i < res[0]:
                res.insert(0, i)
            else:
                for j in range(len(res) - 1):
                    if i == res[j]:
                        res.insert(j + 1, i)
                        break
                    elif res[j] < i < res[j + 1]:
                        res.insert(j + 1, i)
                        break
    return res

nums = [1,43,1,23980980,4,1123,4,12,3]
sorted_nums = insertion_sort(nums)
print(sorted_nums)