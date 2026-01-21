#review
def arrayNesting(nums):
    seen = set()
    best = 0

    for i in range(len(nums)):
        if i in seen:
            continue
        
        cur = i
        length = 0

        while cur not in seen:
            seen.add(cur)
            cur = nums[cur]
            length += 1

        best = max(best, length)
    
    return best



            

