def valid_palindrome(s):
    n = len(s)
    left, right = 0, n - 1

    while left <= right:
        if s[left].lower != s[right].lower():
            return False
            
    return True