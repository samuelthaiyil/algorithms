def longestSequence(nums):
    nums_set = set(nums)
    best = 0

    for i in range(len(nums)):
        if i - 1 not in nums_set:
            length = 1
            curr = i

            while curr in nums_set:
                length += 1
                curr += 1
            
            best = max(best, length)
    
    return best
            
