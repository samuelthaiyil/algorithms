def longestCOnsecutive(nums):
    nums_set = set(nums)
    longest = 0

    for n in nums_set:
        if n - 1 not in nums_set:
            length = 1
            cur = n
            
            while cur + 1 in nums_set:
                cur += 1
                length += 1
            
            longest = max(longest, length)
    
    return longest

