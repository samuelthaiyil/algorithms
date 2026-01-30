def maxSubarray(nums):
    max_subarray = float("-inf")

    # set pivot
    for i in range(len(nums)):
        curr_subarray = 0
        for j in range(i, len(nums)):
            curr_subarray += nums[j]
            max_subarray = max(max_subarray, curr_subarray)
    
    return max_subarray