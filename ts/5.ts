function kFrequentElements(arr: number[], k: number): number[] {
  const frequencies = new Map<number, number>();

  for (const num of arr) {
    if (!frequencies.has(num)) {
      frequencies.set(num, 1);
      continue;
    }
    frequencies.set(num, frequencies.get(num)! + 1);
  }

  const results = [];
  const temp = [...frequencies.values()].sort().reverse();

  console.log(frequencies);
  console.log(temp);
  
  for (const num of temp) {
    for (const [key, value] of frequencies.entries()) {
      if (num === value) {
        results.push(key);
      }
    }
  }

  return results.slice(0, k);
}

console.log(kFrequentElements([1, 2, 2, 3, 3, 3], 2));
