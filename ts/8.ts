function longestConsecutiveSequence(arr: number[]) {
  arr.sort((a, b) => a - b);
  let diff = 1;
  const results = [];

  for (const [index, num] of arr.entries()) {
    if (index !== 0) {
      if (arr[index]! === arr[index - 1]!) {
        continue;
      }
      diff = arr[index]! - arr[index - 1]!;
    }
    if (diff !== 1) {
      break;
    }
    results.push(num);
  }

  return results.length;
}

console.log(longestConsecutiveSequence([0,3,2,5,4,6,1,1]));
