def longestSubstring(s):
    ss = set()
    left, best = 0, 0
    n = len(s)

    for right in range(n):
        while s[right] in ss:
            ss.remove(s[left])
            left += 1
        
        ss.add(s[right])

        # add 1 since 0-indexed
        best = max(best, (right - left) + 1)
    
    return best