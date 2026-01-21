def valid_palindrome(str):
    l, r = 0, len(str) - 1

    while l < r:
        l += 1
        r -= 1
        if str[l] != str[r]:
            return False
    return True
        
print(valid_palindrome("caddsac"))
        
