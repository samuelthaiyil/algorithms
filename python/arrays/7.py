def palindrome_number(num):
    n = len(str(num))
    left, right = 0, n - 1

    while left <= right:
        if str(num[left]) != str(num[right]):
            return False
        left += 1
        right -= 1
    
    return True