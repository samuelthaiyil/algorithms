def isSubsequence(s, t):
    if len(s) == 0:
            return True
    elif len(t) == 0:
        return False

    index = 0

    for c in t:
        if s[index] == c:
            index += 1
        if len(s) == index:
            return True
    
    return False

print(isSubsequence("abc", "ahbgdc"))
