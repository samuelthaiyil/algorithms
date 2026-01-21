def product_of_array_except_self(arr):
    n = len(arr)
    res = [0] * n
    
    for i in range(n):
        prod = 1
        for j in range(n):
            if i == j:
                continue
            prod *= arr[j]
        res[i] = prod
    
    return res  

print(product_of_array_except_self([-1,0,1,2,3]))