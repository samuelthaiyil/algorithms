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
    
    for i in frequencies.values():
        if i != 0:
            return False

    return True

print(is_anagram("racecar", "carrace"))