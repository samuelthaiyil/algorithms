def group_anagram(strs):
    def is_anagram(l, s):
        char_frequencies = dict()

        for c in l:
            if c not in char_frequencies:
                char_frequencies[c] = 1
                continue
            char_frequencies[c] += 1
        
        for c in s:
            if c not in char_frequencies:
                return False
            char_frequencies[c] -= 1
        
        for value in char_frequencies.values():
            if value != 0:
                return False

        return True
    
    res = []

    for s in strs:
        if len(res) == 0:
            res.append([strs[0]])
            continue
        found = False
        for g in res:
            if is_anagram(s, g[0]):
                g.append(s)
                found = True
                break
        if not found:
            res.append([s])
    
    return res

print(group_anagram(["a"]))


        


        


