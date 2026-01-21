def myAtoi(s):
    sign = 1
    index = 0
    n = len(s)

    result = 0

    INT_MIN = -(2**31)
    INT_MAX = (2**31) - 1

    # remove leading spaces
    while s[index] == " ":
        index += 1
    
    if s[index] == "-":
        sign = -1
        index += 1
    elif s[index] == "+":
        index += 1

    while index < n and s[index] == "0":
        index += 1
    
    while index < n and s[index].isdigit():        
        signed = sign * result

        if signed > INT_MAX:
            return INT_MAX
        elif signed < INT_MIN:
            return INT_MIN

        result = 10 * result + int(s[index])
        index += 1

    return sign * result

print(myAtoi("42"))
        
