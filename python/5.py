def two_sum(arr, target):
    for i in arr:
        s = target - i
        if s in arr:
            return [arr.index(i), arr.index(s)]
    
    return [-1, -1]

print(two_sum([3,1,5,8], 7))



        
