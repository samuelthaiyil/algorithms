def reverse_string(s):
    res = ""
    
    n = len(s)
    i = n - 1

    while i >= 0:
        res += s[i]
        i -= 1
    
    return res

print(reverse_string("Cat"))