def plus_one(nums):
    res = nums.copy()

    n = len(nums)
    i = n - 1

    while i >= 0:
        if res[i] == 9:
            res[i] = 0
        else: 
            res[i] += 1
            return res
        i -= 1

    return [1] + res

print(plus_one([1,2,3]))