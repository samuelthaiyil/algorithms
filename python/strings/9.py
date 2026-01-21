def longestSubstring(s):
    substr = set()
    left, best = 0, 0

    for right in range(len(s)):
        while s[right] in substr:
            substr.remove(s[left])
            left += 1
        
        substr.add(s[right])
        best = max(best, right - left + 1)
    
    return best

