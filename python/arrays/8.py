def find_k_distance(nums, key, k):
    res = []
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[j] == key and abs(i - j) == k:
                res.append(i)
                break
    return res
