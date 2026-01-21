def min_operations(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 0:
            del nums[i]

    return len(set(nums))

print(min_operations([1,5,0,3,5]))