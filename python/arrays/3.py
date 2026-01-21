def running_sum(nums):
    sum, res = 0, []

    for i in nums:
        res.append(i + sum)
        sum += i
    return res

print(running_sum([1,2,3,4]))