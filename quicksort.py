def quicksort(arr, pivot = None):
    if len(arr) > 1:
        if pivot == None:
            pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return (quicksort(less) + [pivot] + quicksort(greater))
    else:
        return arr

nums = [1,43,1,23,4,1123,4,12,3]
sorted_nums = quicksort(nums)
print(sorted_nums)
