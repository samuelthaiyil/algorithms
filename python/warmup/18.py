def longestSequence(nums):
    nums_set = set(nums)
    best = 0

    for i in nums_set:
        if i - 1 not in nums_set:
            length = 1
            curr = i

            while curr + 1 in nums_set:
                curr += 1
                length += 1
            
            best = max(best, length)
    
    return best
            
