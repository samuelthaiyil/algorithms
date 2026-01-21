def has_duplicates(arr):
    result = set()
    for i in arr:
        if i in result:
            return True
        result.add(i)
    return False

print(has_duplicates([1,2,3]))
