def isPalindrome(s: str):
    res = []

    for ch in s:
        if ch.isalpha() and not ch.isdigit():
            res.append(ch.lower())
    
    res = "".join(res)
    left, right = 0, len(res) - 1

    while left <= right:
        if res[left] != res[right]:
            return False
        left += 1
        right -= 1
    
    return True



print(isPalindrome("A man, a plan, a canal: Panama"))