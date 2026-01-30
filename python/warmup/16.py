def missingNumber(nums):
    nums.sort()

    if nums[0] != 0:
        return 0
    
    if nums[-1] != len(nums):
        return len(nums)
    
    for i in range(1, len(nums) - 1):
        expected = i

        if nums[i] != expected:
            return expected
