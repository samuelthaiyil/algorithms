# m is pattern length, k is times repeated
def containsPattern(arr, m, k):
    n = len(arr)

    # amount of elements needed to pass pattern check
    needed = m * (k - 1)
    # amount of elements that pass pattern checl
    count = 0

    for i in range(n - m):
        if arr[i] == arr[i + m]:
            count += 1
            if count >= needed:
                return True
        else:
            count = 0
    
    return False

