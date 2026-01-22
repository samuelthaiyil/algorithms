def encode(strs):
    """Encodes a list of strings to a single string.
    """
    res = ""
    
    for s in strs:
        res += str(len(s)) + ","
    
    res += "#"

    for s in strs:
        res += s + ","
    
    print(res)
    return res

def decode(s: str):
    """Decodes a single string to a list of strings.
    """
    sizes = []
    strs = []

    i = 0

    # go until we reach EOS or encounter a #
    while i < len(s) and s[i] != "#":
        # create cur to hold parsed size
        cur = 0

        # go until we reach EOS or encounter a ,
        while i < len(s) and s[i] != ",":
            # for each digit add it to curr
            print(s[i])
            cur += (cur * 10) + int(s[i])

            # move the pointer onward
            i += 1

        # once we encounter a , add the parsed size to sizes
        sizes.append(cur)

        # move the pointer onward
        i += 1
    
    # move passed #
    i += 1
    print(sizes)
    print(s[i:])

    # for sz in sizes
    for sz in sizes:
        # append to strs the s from index i to sz - 1
        strs.append(s[i:(i + sz)])
        
        # move index to end of size and passed comma
        i += sz + 1
    
    # return strs
    return strs

print(decode(encode(["Hello", "World"])))