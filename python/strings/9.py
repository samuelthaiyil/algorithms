def longestSubstring(s):
    unique = set()
    left, best = 0, 0

    for right in range(len(s)):
        while s[right] in unique:
            unique.remove(s[left])
            left += 1
        
        unique.append(s[right])
        best = max(best, (right - left) + 1)
    
    return best

