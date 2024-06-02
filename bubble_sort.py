def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j] , arr[j + 1]

    return arr

nums = [1,43,1,23980980,4,1123,4,12,3]
sorted_nums = bubble_sort(nums)
print(sorted_nums)