def maxProduct(nums):
    n = len(nums)
    min_so_far, max_so_far = nums[0]
    result = 0

    for i in range(1, n):
        curr = nums[i]

        temp_max = max(curr, max(max_so_far * curr, min_so_far * curr))
        min_so_far = max(curr, min(max_so_far * curr, min_so_far * curr))

        max_so_far = temp_max
        result = max(max_so_far, result)
    
    return result
