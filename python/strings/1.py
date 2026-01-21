def repeatedSubstringPattern(s):
    n = len(s)

    # iterating over range of substring indices, minimum is 1 and 
    # maximum is n // 2 + 1, we can't have one with an index larger
    for i in range(1, n // 2 + 1):
        # check if 0 to i is a potential substring length
        if n % i == 0:
            # set pattern to substring of s from 0 to i 
            # repeat it n // i times
            pattern = s[:i] * (n // i)

            # check if our pattern is correct
            if s == pattern:
                return True
    return False

print(repeatedSubstringPattern("abcabab"))