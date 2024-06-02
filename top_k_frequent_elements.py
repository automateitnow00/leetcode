"""Given an integer array nums and an integer k, 
return the k most frequent elements. You may return the answer in any order."""


#my solution
def topKFrequent(nums, k: int):
    setnum = set(nums)
    res = []
    for i in setnum:
        x = (i, nums.count(i))
        res.append(x)

    res = sorted(res, key = lambda kv:-kv[1])
    #print(res)
    out = []
    i = 0
    while k > 0:
        out.append(res[i][0])
        i += 1
        k -= 1
    return out

a = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,4,45,2,3,3,4,5,65,66,6,67,7,7,7,7]
print(topKFrequent(a, 3))