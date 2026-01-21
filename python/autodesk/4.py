def is_palindrome(s: str): 
    n = len(s)
    left, right = 0, n - 1

    while left <= right:
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("cac"))