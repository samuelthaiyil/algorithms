def sum_in_arr(nums, target):
    res = []

    for index, i in nums:
        if (target - i) in nums:
            res.append(index)
            res.append(target - i)

    return res