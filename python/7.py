def top_k_elements(arr, k):
    frequencies = dict()

    for i in arr:
        if i not in frequencies:
            frequencies[i] = 1
            continue
        frequencies[i] += 1

    sorted_freq = list(reversed(sorted(frequencies.items(), key=lambda x: x[1])))
    results = []
    
    for number, _ in sorted_freq:
        results.append(number)

    return results[:k]

print(top_k_elements([1,2,2,3,3,3], 2))