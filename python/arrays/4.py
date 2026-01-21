def missing_number(nums):
    nums.sort()

    n = len(nums)

    if nums[-1] != len(nums):
        return len(nums)
    elif nums[0] != 0:
        return nums[0]

    for i in range(1, n):
        expected_num = nums[i - 1] + 1 
        if nums[i] != expected_num:
            return expected_num

print(missing_number([3,0,1]))