def encode(arr):
    res = ""

    for s in arr:
        res += str(len(s)) + ","
    
    res += "#"
    
    for s in arr:
        res += (s + ",")
    
    return res

def decode(s):
    if not s:
        return []
    
    sizes, res, i = [], [], 0

    while s[i] != "#":
        cur = ""
        while s[i] != ",":
            cur += s[i]
            i += 1
        sizes.append(int(cur))
        i += 1
    
    i += 1

    for sz in sizes:
        res.append(str(s[i:i + sz]))
        i += sz + 1
    
    return res

print(decode(encode(["neet","code","love","you"])))





        
