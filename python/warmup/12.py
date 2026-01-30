def maxProduct(nums):
    n = len(nums)
    min_so_far, max_so_far = nums[0], nums[0]
    best = max_so_far

    for i in range(n):
        curr = nums[i]
        
        temp_max = max(curr, max(max_so_far * curr, min_so_far * curr))
        min_so_far = min(curr, min(max_so_far * curr, min_so_far * curr))

        max_so_far = temp_max

        best = max(best, max_so_far)

    return best
