def group_anagrams(arr):
    def is_anagram(l, s):
        frequencies = dict()

        for i in l:
            if i not in frequencies:
                frequencies[i] = 1
                continue
            frequencies[i] += 1
        
        for i in s:
            if i not in frequencies:
                return False
            frequencies[i] -= 1
        
        for c in frequencies.values():
            if c != 0:
                return False
        
        return True
    
    results = []

    for s in arr:
        found = False
        if len(results) == 0:
            results.append([s])
            continue
        for g in results:
            if is_anagram(g[0], s):
                g.append(s)
                found = True
        if found == False:
            results.append([s])
    
    return results

print(group_anagrams(["act","pots","tops","cat","stop","hat"]))