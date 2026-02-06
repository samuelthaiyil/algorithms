def maxSubarray(nums):
    max_arr = float("-inf")
    
    for i in range(len(nums)):
        curr_subarray = 0
        for j in range(i, len(nums)):
            curr_subarray += nums[j]
            max_arr = max(max_arr, curr_subarray)

    return max_arr