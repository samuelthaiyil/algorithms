def validAnagram(s, t):
    mappings = dict()

    for ch in s:
        if ch not in mappings:
            mappings[ch] = 1
            continue

        mappings[ch] += 1
    
    for ch in t:
        if ch not in mappings:
            return False
        
        mappings[ch] -= 1
    
    for v in mappings.values():
        if v != 0:
            return False
    
    return True
        